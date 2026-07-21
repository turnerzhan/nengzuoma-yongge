# 贡献指南 · 能做吗？勇哥

感谢你愿意让更多人少踩开店的坑。

## 怎么参与

| 类型 | 怎么交 |
|------|--------|
| Bug / 工具算错 | Issue，附命令与输入输出 JSON |
| 新案例 | 按 `cases/` 现有模板：金额、品类、地点、结果、启示 |
| 方法论补强 | PR 改 `corpus/`，注明依据与场景 |
| 文案/SEO | PR 改 `README.md` / `llms.txt` / `docs/SEO.md` |
| 地图协议 | PR 改 `SKILL.md` 第 6 节，附实测城市 |

## PR 要求

1. 小步提交，中英文 commit 清晰  
2. 不引入「保证赚钱」类话术  
3. 案例必须可核对（公开信息或脱敏自述）  
4. 算账改动请附 `tools/` 命令复现  

## 开发自检

```bash
python tools/breakeven.py --daily-revenue 800 --daily-food-cost 250 \
  --rent 8000 --labor 9000 --category 奶茶
python tools/profit_model.py iron --rent 10000
python tools/match_case.py --amount 600000 --category 汉堡 --location 县城
```

## 行为准则

- 站小经营者，不帮加盟话术洗地  
- 对真实困难者不嘲讽  
- 不冒充任何真人/机构官方  
