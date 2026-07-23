#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
保本线 / 房租铁律 / 开店前反推 · 能做吗？勇哥

用法：
  # 有流水（默认，兼容旧参数）
  python tools/breakeven.py --daily-revenue 800 --daily-food-cost 250 \\
      --rent 8000 --labor 9000 --investment 350000 --category 奶茶

  python tools/breakeven.py run --daily-revenue 800 --rent 8000 --labor 9000 --category 奶茶
  python tools/breakeven.py plan --rent 12000 --labor 9000 --investment 600000 --category 汉堡
  python tools/breakeven.py iron --rent 10000
"""

from __future__ import annotations

import argparse
import json
import sys

CATEGORY_DEFAULT_GROSS_MARGIN: dict[str, float] = {
    "快餐": 0.52,
    "小吃": 0.55,
    "正餐": 0.60,
    "火锅": 0.65,
    "烧烤": 0.60,
    "奶茶": 0.72,
    "饮品": 0.72,
    "咖啡": 0.75,
    "烘焙": 0.65,
    "早餐": 0.55,
}


def rent_iron_law(rent: float) -> dict:
    return {
        "rent": rent,
        "iron_daily_revenue_target": round(rent * 0.3, 2),
        "iron_monthly_revenue_target": round(rent * 9, 2),
        "rule": "合理日营业额 ≈ 月房租 × 0.3；月营业额 ≈ 月房租 × 9",
    }


def calc(
    daily_revenue: float,
    daily_food_cost: float | None,
    rent: float,
    labor: float,
    utilities: float = 1500,
    investment: float | None = None,
    category: str = "快餐",
    gross_margin: float | None = None,
) -> dict:
    if gross_margin is None:
        if daily_food_cost is not None and daily_revenue > 0:
            gross_margin = (daily_revenue - daily_food_cost) / daily_revenue
        else:
            gross_margin = CATEGORY_DEFAULT_GROSS_MARGIN.get(category, 0.55)

    monthly_fixed = rent + labor + utilities
    monthly_breakeven = monthly_fixed / gross_margin if gross_margin > 0 else float("inf")
    daily_breakeven = monthly_breakeven / 30
    achievement = daily_revenue / daily_breakeven if daily_breakeven > 0 else 0

    if achievement < 0.6:
        status, verdict = "🔴 韭菜斩杀线", "做不了。这店从你开的那一刻就已经死了。"
    elif achievement < 0.8:
        status, verdict = "🟠 持续亏损", "再不动就埋了。一个月内冲不到保本线就关。"
    elif achievement < 1.0:
        status, verdict = "🟡 接近保本", "还有救，但必须立刻调整。"
    elif achievement < 1.2:
        status, verdict = "🟢 健康小赚", "稳住，再优化能更好。"
    else:
        status, verdict = "🟢🟢 充裕盈利", "没问题，这家店可以。"

    monthly_revenue = daily_revenue * 30
    monthly_gross = monthly_revenue * gross_margin
    monthly_profit = monthly_gross - monthly_fixed

    flags: list[str] = []
    if rent > monthly_revenue * 0.20:
        flags.append("🔴 房租占比 >20%")
    if daily_food_cost and daily_revenue > 0 and daily_food_cost / daily_revenue > 0.50:
        flags.append("🔴 食材成本率 >50%")
    if monthly_profit < 0:
        flags.append("🔴 月净亏损")

    payback = None
    if investment and monthly_profit > 0:
        payback = investment / monthly_profit
        if payback > 24:
            flags.append("🔴 回本周期 >24 月")

    iron = rent_iron_law(rent)
    if daily_revenue < iron["iron_daily_revenue_target"] * 0.8:
        flags.append("🔴 日流水远低于房租铁律目标")

    return {
        "mode": "run",
        "gross_margin": round(gross_margin, 4),
        "monthly_fixed": round(monthly_fixed, 2),
        "daily_breakeven": round(daily_breakeven, 2),
        "monthly_breakeven": round(monthly_breakeven, 2),
        "achievement_rate": round(achievement, 4),
        "status": status,
        "monthly_revenue_estimate": round(monthly_revenue, 2),
        "monthly_profit_estimate": round(monthly_profit, 2),
        "payback_months": round(payback, 1) if payback else None,
        "rent_iron_law": iron,
        "risk_flags": flags,
        "yongge_verdict": verdict,
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

    payback = None
    if investment and investment > 0 and target_payback_months > 0:
        need_monthly_profit = investment / target_payback_months
        need_daily = (need_monthly_profit + monthly_fixed) / (30 * gm) if gm > 0 else float("inf")
        payback = {
            "target_payback_months": target_payback_months,
            "need_monthly_profit": round(need_monthly_profit, 2),
            "need_daily_revenue_for_payback": round(need_daily, 2),
        }

    floor = max(daily_breakeven, iron["iron_daily_revenue_target"])
    if payback:
        floor = max(floor, payback["need_daily_revenue_for_payback"])

    flags: list[str] = []
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
        "minimum_daily_revenue_gate": round(floor, 2),
        "risk_flags": flags,
        "yongge_verdict": (
            f"没开之前先算：日流水冲不到约 {round(floor)} 元，这模型就别签。"
            if floor < float("inf")
            else "参数不足，算不出。"
        ),
    }


def _add_run_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--daily-revenue", type=float, required=True)
    p.add_argument("--daily-food-cost", type=float, default=None)
    p.add_argument("--rent", type=float, required=True)
    p.add_argument("--labor", type=float, required=True)
    p.add_argument("--utilities", type=float, default=1500)
    p.add_argument("--investment", type=float, default=None)
    p.add_argument("--category", default="快餐")
    p.add_argument("--gross-margin", type=float, default=None)


def main() -> None:
    argv = sys.argv[1:]
    # 兼容旧调用：无子命令时当作 run
    if not argv or (argv[0] not in ("run", "plan", "iron", "-h", "--help") and argv[0].startswith("-")):
        p = argparse.ArgumentParser(description="能做吗？勇哥 · 保本线")
        _add_run_args(p)
        args = p.parse_args(argv)
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
    else:
        p = argparse.ArgumentParser(description="能做吗？勇哥 · 保本线")
        sub = p.add_subparsers(dest="cmd", required=True)
        run_p = sub.add_parser("run", help="有流水：保本体检")
        _add_run_args(run_p)
        plan_p = sub.add_parser("plan", help="开店前：反推日流水门槛")
        plan_p.add_argument("--rent", type=float, required=True)
        plan_p.add_argument("--labor", type=float, required=True)
        plan_p.add_argument("--utilities", type=float, default=1500)
        plan_p.add_argument("--investment", type=float, default=None)
        plan_p.add_argument("--category", default="快餐")
        plan_p.add_argument("--gross-margin", type=float, default=None)
        plan_p.add_argument("--target-payback-months", type=float, default=18)
        iron_p = sub.add_parser("iron", help="房租铁律")
        iron_p.add_argument("--rent", type=float, required=True)
        args = p.parse_args(argv)
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
