#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快招（快速招商加盟）风险评分器

用法：
    python tools/quack_score.py \\
        --source "抖音广告" \\
        --hq-city "济南" \\
        --total-fee 580000 \\
        --direct-stores 2 \\
        --years 1 \\
        --promises "零加盟费,6个月回本,总部全包"

输出 JSON。
"""

from __future__ import annotations
import argparse
import json
import sys

HIGH_RISK_CITIES = {"济南"}
MID_RISK_CITIES = {"杭州", "上海", "郑州", "武汉", "长沙"}
RED_PROMISES = {"零加盟费", "6个月回本", "六个月回本", "总部全包", "保姆式扶持"}


def score(
    source: str,
    hq_city: str,
    total_fee: float,
    direct_stores: int,
    years: float,
    promises: list[str],
) -> dict:
    s = 0
    reasons = []

    src = source.lower()
    if any(k in src for k in ("广告", "抖音", "小红书", "搜索", "百度", "短视频")):
        s += 1; reasons.append("+1 来源是广告/短视频/搜索引擎")

    if hq_city in HIGH_RISK_CITIES:
        s += 2; reasons.append("+2 总部在济南（最高警报）")
    elif hq_city in MID_RISK_CITIES:
        s += 1; reasons.append(f"+1 总部在 {hq_city}（高警报）")

    if total_fee > 300_000:
        s += 2; reasons.append("+2 一次性投入 >30 万")
    elif total_fee > 100_000:
        s += 1; reasons.append("+1 一次性投入 >10 万")

    if direct_stores < 5 or years < 1:
        s += 2; reasons.append("+2 直营店<5 家或经营<1 年")
    elif direct_stores < 10:
        s += 1; reasons.append("+1 直营店<10 家")

    hit_promises = [p for p in promises if p.replace(" ", "") in {x.replace(" ", "") for x in RED_PROMISES}]
    if hit_promises:
        s += 2; reasons.append(f"+2 命中红线话术：{hit_promises}")

    if s >= 5:
        level, verdict = "🔴 高度疑似快招", "强烈建议放弃。已打款的留好证据，该起诉起诉。"
    elif s >= 3:
        level, verdict = "🟠 有疑点", "必须实地验证 + 工商核查再做决定。"
    else:
        level, verdict = "🟡 相对可控", "仍需常规尽调（直营店探访、企查查）。"

    return {
        "score": s,
        "level": level,
        "reasons": reasons,
        "yongge_verdict": verdict,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", required=True)
    p.add_argument("--hq-city", required=True)
    p.add_argument("--total-fee", type=float, required=True)
    p.add_argument("--direct-stores", type=int, default=0)
    p.add_argument("--years", type=float, default=0)
    p.add_argument("--promises", default="", help="逗号分隔的承诺话术")
    args = p.parse_args()

    promises = [x.strip() for x in args.promises.split(",") if x.strip()]
    result = score(
        source=args.source,
        hq_city=args.hq_city,
        total_fee=args.total_fee,
        direct_stores=args.direct_stores,
        years=args.years,
        promises=promises,
    )
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
