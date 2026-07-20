#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
盈利 / 选址财务模型 · 「能做吗？勇哥」

在原版保本线之外，补齐开店前场景（还没流水）的反推：
- 日保本线
- 房租铁律目标流水
- 总投入回本压力

用法示例：
  # 已营业（或给了预估日流水）
  python scripts/profit_model.py run \\
    --daily-revenue 800 --daily-food-cost 250 \\
    --rent 8000 --labor 9000 --investment 350000 --category 奶茶

  # 开店前：只有租、人工、总投入、品类 → 反推必须卖多少
  python scripts/profit_model.py plan \\
    --rent 12000 --labor 9000 --investment 600000 --category 汉堡

输出 JSON。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# 复用同目录 breakeven
# same-dir import
from breakeven import CATEGORY_DEFAULT_GROSS_MARGIN, calc  # noqa: E402


def rent_iron_law(rent: float) -> dict:
    """勇哥：1 万房租 ≈ 日营业额 3000 → 日 ≈ 月租×0.3，月 ≈ 月租×9"""
    daily_target = rent * 0.3
    monthly_target = rent * 9
    return {
        "rent": rent,
        "iron_daily_revenue_target": round(daily_target, 2),
        "iron_monthly_revenue_target": round(monthly_target, 2),
        "rule": "合理日营业额 ≈ 月房租 × 0.3；月营业额 ≈ 月房租 × 9（房租约占 11%）",
    }


def plan(
    rent: float,
    labor: float,
    utilities: float = 1500,
    investment: float | None = None,
    category: str = "快餐",
    gross_margin: float | None = None,
    target_payback_months: float = 18,
) -> dict:
    gm = gross_margin if gross_margin is not None else CATEGORY_DEFAULT_GROSS_MARGIN.get(category, 0.55)
    monthly_fixed = rent + labor + utilities
    monthly_breakeven = monthly_fixed / gm if gm > 0 else float("inf")
    daily_breakeven = monthly_breakeven / 30

    iron = rent_iron_law(rent)

    # 若要在 target_payback_months 回本，需要的月净利 / 日营收
    payback = None
    if investment and investment > 0 and target_payback_months > 0:
        need_monthly_profit = investment / target_payback_months
        # 月净利 = 月营收×毛利率 - 固定；月营收 = 日营收×30
        # need_monthly_profit = daily*30*gm - fixed
        # daily = (need_monthly_profit + fixed) / (30*gm)
        need_daily_for_payback = (need_monthly_profit + monthly_fixed) / (30 * gm) if gm > 0 else float("inf")
        payback = {
            "target_payback_months": target_payback_months,
            "need_monthly_profit": round(need_monthly_profit, 2),
            "need_daily_revenue_for_payback": round(need_daily_for_payback, 2),
        }

    # 取「铁律目标」与「保本线」更严者作为最低日流水门槛
    floor_daily = max(daily_breakeven, iron["iron_daily_revenue_target"])
    if payback:
        floor_daily = max(floor_daily, payback["need_daily_revenue_for_payback"])

    flags = []
    if daily_breakeven > iron["iron_daily_revenue_target"] * 1.2:
        flags.append("🔴 固定成本过高：保本线明显高于房租铁律目标")
    if investment and investment >= 300_000:
        flags.append("🟠 总投入 ≥30 万，回本压力大")
    if investment and investment >= 500_000:
        flags.append("🔴 总投入 ≥50 万，小白默认劝退档")

    return {
        "mode": "plan",
        "category": category,
        "gross_margin_assumed": round(gm, 4),
        "monthly_fixed": round(monthly_fixed, 2),
        "daily_breakeven": round(daily_breakeven, 2),
        "monthly_breakeven": round(monthly_breakeven, 2),
        "rent_iron_law": iron,
        "payback_pressure": payback,
        "minimum_daily_revenue_gate": round(floor_daily, 2),
        "risk_flags": flags,
        "yongge_verdict": (
            f"没开之前先算：日流水冲不到约 {round(floor_daily)} 元，这模型就别签。"
            if floor_daily < float("inf")
            else "参数不足，算不出。"
        ),
        "formula": {
            "monthly_fixed": "房租 + 人工 + 水电杂项",
            "daily_breakeven": "月固定支出 ÷ 毛利率 ÷ 30",
            "rent_iron": "日目标 ≈ 月租 × 0.3",
            "payback_daily": "(总投入/目标月数 + 月固定) ÷ (30 × 毛利率)",
        },
    }


def main() -> None:
    p = argparse.ArgumentParser(description="能做吗？勇哥 · 盈利模型")
    sub = p.add_subparsers(dest="cmd", required=True)

    run_p = sub.add_parser("run", help="已有/预估日流水：保本线体检")
    run_p.add_argument("--daily-revenue", type=float, required=True)
    run_p.add_argument("--daily-food-cost", type=float, default=None)
    run_p.add_argument("--rent", type=float, required=True)
    run_p.add_argument("--labor", type=float, required=True)
    run_p.add_argument("--utilities", type=float, default=1500)
    run_p.add_argument("--investment", type=float, default=None)
    run_p.add_argument("--category", default="快餐")
    run_p.add_argument("--gross-margin", type=float, default=None)

    plan_p = sub.add_parser("plan", help="开店前：反推必须卖多少")
    plan_p.add_argument("--rent", type=float, required=True)
    plan_p.add_argument("--labor", type=float, required=True)
    plan_p.add_argument("--utilities", type=float, default=1500)
    plan_p.add_argument("--investment", type=float, default=None)
    plan_p.add_argument("--category", default="快餐")
    plan_p.add_argument("--gross-margin", type=float, default=None)
    plan_p.add_argument("--target-payback-months", type=float, default=18)

    iron_p = sub.add_parser("iron", help="只算房租铁律")
    iron_p.add_argument("--rent", type=float, required=True)

    args = p.parse_args()
    if args.cmd == "run":
        result = calc(
            daily_revenue=args.daily_revenue,
            daily_food_cost=args.daily_food_cost,
            rent=args.rent,
            labor=args.labor,
            utilities=args.utilities,
            investment=args.investment,
            category=args.category,
            gross_margin=args.gross_margin,
        )
        result["mode"] = "run"
        result["rent_iron_law"] = rent_iron_law(args.rent)
        # 对照铁律
        if args.daily_revenue < result["rent_iron_law"]["iron_daily_revenue_target"] * 0.8:
            result.setdefault("risk_flags", []).append("🔴 日流水远低于房租铁律目标")
    elif args.cmd == "plan":
        result = plan(
            rent=args.rent,
            labor=args.labor,
            utilities=args.utilities,
            investment=args.investment,
            category=args.category,
            gross_margin=args.gross_margin,
            target_payback_months=args.target_payback_months,
        )
    else:
        result = rent_iron_law(args.rent)

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
