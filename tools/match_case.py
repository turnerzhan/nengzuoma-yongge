#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
案例匹配器 · 给定金额/品类/选址类型，返回最相近的案例

用法：
    python tools/match_case.py --amount 900000 --category 奶茶 --location 县城
"""

from __future__ import annotations
import argparse
import json
import sys


CASES = [
    {
        "id": "001", "name": "脸盆姐 · 济南果汁",
        "amount": 20000, "category": "饮品", "location": "城市",
        "tags": ["蜜雪旁边", "杂牌饮品", "自杀式选址"],
        "path": "cases/失败案例/001-脸盆姐-济南果汁.md",
    },
    {
        "id": "002", "name": "七层奶茶大厦 · 长治",
        "amount": 900000, "category": "奶茶", "location": "县城",
        "tags": ["重资产", "抵押贷款", "边缘选址", "快招", "多业态"],
        "path": "cases/失败案例/002-七层奶茶大厦-长治.md",
    },
    {
        "id": "003", "name": "第四代汉堡 · 宁夏 6 天 90 万",
        "amount": 900000, "category": "汉堡", "location": "城市",
        "tags": ["快招", "庞氏代理", "总部济南类", "迅速失败"],
        "path": "cases/失败案例/003-第四代汉堡-宁夏.md",
    },
    {
        "id": "004", "name": "哪吒仙饮 · 宝妈陷阱",
        "amount": 300000, "category": "概念奶茶", "location": "全国",
        "tags": ["IP借势", "宝妈群体", "新型快招"],
        "path": "cases/失败案例/004-哪吒仙饮.md",
    },
    {
        "id": "005", "name": "家是本 · 成都葱油饼",
        "amount": 100000, "category": "小吃", "location": "城市",
        "tags": ["概念抽象", "葱油饼", "门头满文字"],
        "path": "cases/失败案例/005-家是本-成都葱油饼.md",
    },
    {
        "id": "006", "name": "两江总督 · 江西",
        "amount": 550000, "category": "饮品", "location": "省级",
        "tags": ["区域代理", "庞氏", "抵押住房"],
        "path": "cases/失败案例/006-两江总督.md",
    },
    {
        "id": "007", "name": "自嗨哥 · 北京",
        "amount": 1000000, "category": "减脂餐", "location": "一线",
        "tags": ["不听劝", "连续亏损", "高客单"],
        "path": "cases/失败案例/007-自嗨哥.md",
    },
    {
        "id": "011", "name": "大学城盖浇饭",
        "amount": 390000, "category": "快餐", "location": "大学城",
        "tags": ["新开发区", "高估流量"],
        "path": "cases/失败案例/011-大学城盖浇饭.md",
    },
    {
        "id": "012", "name": "综合体倒闭位",
        "amount": 200000, "category": "快餐", "location": "综合体",
        "tags": ["商住综合体", "盒马KTV旁", "日销4单"],
        "path": "cases/失败案例/012-综合体倒闭位.md",
    },
    {
        "id": "013", "name": "枣庄烘焙店",
        "amount": 400000, "category": "烘焙", "location": "城市",
        "tags": ["烘焙红海", "加盟", "破产四件套"],
        "path": "cases/失败案例/013-枣庄烘焙店.md",
    },
    {
        "id": "014", "name": "玻尿酸羊乳咖啡",
        "amount": 400000, "category": "概念咖啡", "location": "上海",
        "tags": ["送车骗局", "概念", "新型快招"],
        "path": "cases/失败案例/014-玻尿酸羊乳咖啡.md",
    },
    {
        "id": "021", "name": "韩国咖啡 160 万",
        "amount": 1600000, "category": "咖啡", "location": "城市",
        "tags": ["重资产", "亏一辆迈巴赫"],
        "path": "cases/失败案例/021-韩国咖啡.md",
    },
    {
        "id": "S001", "name": "关起来杀哥 · 封闭学校",
        "amount": 200000, "category": "校园餐饮", "location": "封闭场所",
        "tags": ["垄断选址", "三天回本", "听劝"],
        "path": "cases/成功案例/001-关起来杀哥.md",
        "success": True,
    },
    {
        "id": "S002", "name": "烤面筋小伙",
        "amount": 5000, "category": "小吃", "location": "城市",
        "tags": ["低成本", "刚需", "复制"],
        "path": "cases/成功案例/002-烤面筋小伙.md",
        "success": True,
    },
]


def match(amount: float, category: str, location: str, tags: list[str], top_k: int = 3) -> list[dict]:
    results = []
    for c in CASES:
        score = 0
        if amount > 0:
            ratio = min(amount, c["amount"]) / max(amount, c["amount"])
            score += ratio * 30
        if category and (category in c["category"] or c["category"] in category):
            score += 30
        if location and (location in c["location"] or c["location"] in location):
            score += 20
        if tags:
            overlap = len(set(tags) & set(c["tags"]))
            score += overlap * 10
        results.append({**c, "match_score": round(score, 2)})

    results.sort(key=lambda x: x["match_score"], reverse=True)
    return results[:top_k]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--amount", type=float, default=0)
    p.add_argument("--category", default="")
    p.add_argument("--location", default="")
    p.add_argument("--tags", default="", help="逗号分隔")
    p.add_argument("--top-k", type=int, default=3)
    args = p.parse_args()

    tags = [x.strip() for x in args.tags.split(",") if x.strip()]
    result = match(args.amount, args.category, args.location, tags, args.top_k)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
