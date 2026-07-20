<p align="center">
  <img src="docs/assets/logo.jpg" width="120" alt="能做吗？勇哥" />
</p>

<h1 align="center">能做吗？勇哥</h1>

<p align="center">
  <strong>门头一拍 · 红黄绿判生死</strong><br/>
  用勇哥餐饮方法论武装的 Agent Skill<br/>
  选址 × 业态 × 加盟劝退 — 专为小经营者反踩坑
</p>

<p align="center">
  <a href="https://github.com/turnerzhan/nengzuoma-yongge/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-0A0A0A?style=flat-square" alt="MIT" /></a>
  <a href="#安装"><img src="https://img.shields.io/badge/Agent-Skill-7C1C1C?style=flat-square" alt="Skill" /></a>
  <img src="https://img.shields.io/badge/地图-高德主·百度备-1F2937?style=flat-square" alt="Maps" />
  <img src="https://img.shields.io/badge/version-0.1.0-C4A35A?style=flat-square" alt="version" />
</p>

<p align="center">
  <img src="docs/assets/banner.jpg" width="100%" alt="banner" />
</p>

---

## 为什么做这个

餐饮看起来很火。  
对小经营者来说，火的是话题，冷的是现金流。

大多数店死在开业前没算清的账里：  
**错位置、错业态、假加盟、盖不住的房租。**

> **勇哥说能做的，不能保证赚钱。**  
> **勇哥说不能做的，一定亏钱。**

「能做吗？勇哥」把这套判断，收成一次对话能跑完的 **验铺协议**：  
拍门头、丢地址、说业态——直接给红 / 黄 / 绿，并讲清楚为什么。

它不是鸡汤助手，也不是房东话术生成器。  
它是 **开店前的最后一道闸**。

---

## 30 秒体验

```
你：  [门头照片]
      浙江台州路桥区腾达路699号
      加盟全国首家××汉堡，总投入大概60万

哥：  🔴 做不了（至少这笔加盟别签）

      · 「全国首家」= 你是样本不是加盟商
      · 汉堡属高压赛道，投入已触快招高危区
      · 同走廊有塔斯汀 / 麦当劳 / 华莱士
      · 换业态？社区刚需可谈，这套加盟免谈
```

---

## 产品定位

| | |
|--|--|
| **产品名** | 能做吗？勇哥 |
| **仓库 ID** | `nengzuoma-yongge`（GitHub 仓库名不支持纯中文，见下方说明） |
| **Skill ID** | `nengzuoma-yongge` |
| **一句话** | 门头一拍，能做吗？ |
| **用户** | 想开店 / 已看铺 / 被加盟话术包围的普通人 |
| **不做什么** | 不保证赚钱、不替代律师会计、不站加盟商一边 |

### 架构（一句话）

```text
看图 + 高德(主) + 百度(备)  ──供血──▶  勇哥规则  ──▶  红黄绿 + 动作
```

地图只负责事实；**判断权只在方法论**。

---

## 能力地图

| 模块 | 内容 |
|------|------|
| **门头微观** | 楼层、台阶、遮挡、门头识别、装修/未开业迹象 |
| **商圈供血** | 同业密度、学校/小区/写字楼/商场、大牌贴脸 |
| **业态匹配** | 位置类型 × 业态矩阵；不适配则给替代方向 |
| **财务闸门** | 房租铁律、投入与保本直觉（有数就算） |
| **加盟快诊** | 全国首家、高加盟费、四件套赛道、话术红线 |
| **交付** | 固定报告结构：结论 → 原因 → 换业态 → 现场确认 |

双地图策略：**不默认全量交叉**（数据高度同类且坐标系不同）；  
百度用于 **高德失败兜底** 与 **关键大牌争议抽检**。

---

## 安装

### 1. 克隆

```bash
git clone https://github.com/turnerzhan/nengzuoma-yongge.git
```

### 2. 放入 Agent Skills 目录

| 环境 | 路径示例 |
|------|----------|
| Grok | `~/.grok/skills/nengzuoma-yongge/` |
| Claude | 用户/项目 skills 目录 |
| 通用 | 任何读取 `SKILL.md` frontmatter 的 Agent |

### 3. 运行时依赖

| 依赖 | 级别 |
|------|------|
| 多模态（看图） | 必须 |
| 高德 MCP `amap-maps` | 强推荐 |
| 百度 MCP `baidu-maps` | 推荐（兜底） |
| Python + Pillow | 可选（EXIF） |

```bash
# 可选：读照片 GPS
pip install pillow
python scripts/parse_image_location.py your-storefront.jpg
```

### 4. 触发

- 斜杠：`/nengzuoma-yongge`
- 自然语言：`能做吗`、`勇哥`、`这个铺行不行`、发门头图

---

## 仓库结构

```text
nengzuoma-yongge/
├── SKILL.md                      # Agent 入口（协议）
├── README.md                     # 你正在读
├── LICENSE
├── docs/
│   └── assets/
│       ├── logo.jpg              # 品牌标识
│       └── banner.jpg            # 封面视觉
├── references/
│   ├── yongge-decision-core.md   # 红线 · 选址 · 案例锚点
│   ├── street-score-auto.md      # 可自动打分项
│   ├── category-fit-matrix.md    # 位置 × 业态
│   └── output-template.md        # 输出与语气
└── scripts/
    └── parse_image_location.py
```

---

## 设计原则

1. **劝退优先** — 99% 的人最需要听到「做不了」  
2. **数据 > 感觉** — 没有 POI / 没有数，就降级并写明  
3. **短句结论** — 红黄绿必须一眼可读  
4. **站在普通人** — 不帮房东洗铺，不帮加盟话术圆场  
5. **可解释** — 每条红灯对应规则或地图事实  

---

## 关于仓库中文名

GitHub **仓库 slug 会剥离汉字**（实测：中文名会被收成 `-` / `---`）。  
因此：

| 层 | 命名 |
|----|------|
| **品牌 / 标题** | 能做吗？勇哥 |
| **仓库 URL** | `turnerzhan/nengzuoma-yongge` |
| **Skill `name`** | `nengzuoma-yongge` |

对外传播用中文品牌；工程师克隆用英文 ID。这是平台限制，不是降级。

---

## 方法论渊源与边界

- 判断框架蒸馏自公开传播的「勇哥餐饮」选址 / 诊断逻辑与社区 skill 整理。  
- 参考母体（无官方关联）：[Astro-wen/yongge-restaurant-skill](https://github.com/Astro-wen/yongge-restaurant-skill)  
- **本仓库与「勇哥」本人及原机构无任何官方关系。**  
- 输出为决策辅助，**不构成投资、法律或会计建议**；责任在使用者。

---

## 路线图

- [x] v0.1 门头快诊协议 + 高德主链路  
- [x] 百度兜底配置说明  
- [x] 品牌视觉与公开仓库  
- [ ] 更多城市 demo 与案例锚点  
- [ ] 可选报告 HTML 导出  
- [ ] 关键红线「双源抽检」开关写进协议默认模板  

欢迎 Issue / PR：案例锚点、矩阵校正、地图适配。

---

## License

[MIT](./LICENSE)

---

<p align="center">
  <sub>能做吗？勇哥。</sub><br/>
  <sub>不能做的，别硬开。</sub>
</p>
