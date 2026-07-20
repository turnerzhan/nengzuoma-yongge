<p align="center">
  <img src="docs/assets/logo.png" width="160" alt="能做吗？勇哥" />
</p>

<h1 align="center">能做吗？勇哥</h1>

<p align="center">
  <b>拍一张门头，3 分钟骂醒你。</b><br/>
  <b>全量勇哥方法论</b> · 不是精简版
</p>

<p align="center">
  <img src="https://img.shields.io/badge/🔴_做不了-B91C1C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/内容-全量_corpus+cases-111?style=for-the-badge" />
  <img src="https://img.shields.io/badge/地图-高德主·百度备-1F2937?style=for-the-badge" />
</p>

<p align="center">
  <img src="docs/assets/cover-banner.jpg" width="100%" alt="cover" />
</p>

---

## 重要声明：全量接入，禁止当删减包用

本仓库 **完整收录** 上游 [yongge-restaurant-skill](https://github.com/Astro-wen/yongge-restaurant-skill) 的：

| 目录 | 内容 |
|------|------|
| **`corpus/`** | 9 篇全量方法论（诊断 SOP / 选址 / 快招 / 品类 / 金句 / 常识…） |
| **`cases/`** | 全量失败 + 成功案例库 |
| **`skill/`** | 风格指引 / 提问树 / 街景 12 项 / 保本线文档 |
| **`tools/`** | breakeven / quack_score / match_case（+ 本产品扩展） |

Agent 必须按 `SKILL.md` **按需打开全文**，不得只用 `references/` 摘要偷懒。  
详见 [`THIRD_PARTY.md`](./THIRD_PARTY.md)。

---

## 产品多了什么（在全量之上）

1. **门头快诊入口**：照片 + 地址 → 红黄绿  
2. **高德主 / 百度备** POI 供血（同业、大牌、学校、商场…）  
3. **`tools/profit_model.py`**：开店前反推日流水门槛  
4. **传播壳**：能做吗？勇哥 · 验铺行刑队话术与视觉  

**判断大脑仍是全量勇哥规则 + 案例库 + 算账。**

---

## 30 秒懂

```text
你：门头图 + 地址 + 想加盟/想开啥 + 租与投入
哥：地图事实 + 保本线/铁律 + 全量 SOP + cases 类比
    → 🔴做不了 / 🟡谨慎 / 🟢罕见
```

爽点：**拦你倾家荡产**，不是灌鸡汤发财。

---

## 安装

```bash
git clone https://github.com/turnerzhan/nengzuoma-yongge.git
# 整目录放入 Agent Skills（勿只拷 SKILL.md）
```

| 依赖 | |
|------|--|
| 多模态看图 | 街景/门头 |
| 高德 MCP | 强推 |
| 百度 MCP | 兜底 |
| Python 3 | tools 算账 / 案例匹配 |

触发：`/nengzuoma-yongge` · 能做吗 · 勇哥 · 开店/加盟/保本/门头照

---

## 算账（全量工具）

```bash
python tools/breakeven.py --daily-revenue 800 --daily-food-cost 250 \
  --rent 8000 --labor 9000 --investment 350000 --category 奶茶

python tools/quack_score.py --source "抖音" --hq-city 济南 \
  --total-fee 580000 --direct-stores 2 --years 1 \
  --promises "零加盟费,6个月回本,总部全包"

python tools/match_case.py --amount 900000 --category 奶茶 --location 县城

python tools/profit_model.py plan --rent 12000 --labor 9000 \
  --investment 600000 --category 汉堡
```

---

## 仓库结构

```text
nengzuoma-yongge/
├── SKILL.md              # 全量路由 + 品牌壳 + 地图扩展
├── corpus/               # 全量知识库
├── cases/                # 全量案例
├── skill/                # 全量工程化文档
├── tools/                # 全量计算器 + 扩展
├── references/           # 补充（不得替代 corpus）
├── docs/assets/          # 传播图
└── docs/yongge-upstream/ # 上游架构存档
```

---

## 边界

- 决策辅助，非投资/法律/会计意见  
- 与勇哥本人及原机构 **无官方关联**  
- 地图 POI ≠ 真实客流  

## License

MIT（含上游 MIT 内容，见 `THIRD_PARTY.md`）

---

<p align="center">
  <b>能做吗？勇哥。</b><br/>
  全量武器库已装填。做不了的 —— 今天就停。
</p>
