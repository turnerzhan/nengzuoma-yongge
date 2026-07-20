# 能做吗？勇哥

> 门头一拍，能做吗？——该劝退就劝退。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Skill](https://img.shields.io/badge/Agent-Skill-purple.svg)](#安装)

用**勇哥餐饮选址 / 算账 / 劝退方法论**做判断核心；  
**高德 MCP（主）+ 百度 MCP（兜底/抽检）+ 看图**只负责把路段事实喂饱。

| 项 | 值 |
|----|-----|
| **产品名** | **能做吗？勇哥** |
| **技术 ID** | `nengzuoma-yongge` |
| **斜杠** | `/nengzuoma-yongge` |
| **一句话** | 拍门头 / 丢地址 → 红黄绿 → 说清楚能不能做 |

---

## 用户怎么用

1. 拍一张**门头或街景**（最好含左右路况）  
2. （可选）地址，如：`浙江台州路桥区腾达路699号`  
3. （可选）业态 / 加盟品牌 / 总投入 / 月租  

得到：

- 结论灯（红 / 黄 / 绿）  
- **为什么**（规则 + 地图数据）  
- 换业态建议  
- 现场确认清单  
- 加盟场景下的投入与快招风险提醒  

---

## 演示结论风格（真实案例形态）

> 加盟「全国首家」杂牌汉堡 + 总投入 60 万+ + 吾悦商圈走廊有塔斯汀/麦当劳  
> → **🔴 做不了（至少这笔加盟别签）**

详见 Skill 内方法论：`references/yongge-decision-core.md`。

---

## 安装

### Claude / Cursor / Grok 等 Agent Skills

```bash
git clone https://github.com/turnerzhan/nengzuoma-yongge.git
```

将目录放入 Skills 路径，例如：

- Grok：`~/.grok/skills/nengzuoma-yongge/`
- Claude：项目或用户 skills 目录  

Agent 读取根目录 `SKILL.md` frontmatter（`name` / `description`）完成注册。

### 依赖（运行时）

| 依赖 | 级别 | 说明 |
|------|------|------|
| 多模态（能看图） | 必须 | 无图则需文字描述门头 |
| 高德 MCP `amap-maps` | 强推荐 | 主数据源 |
| 百度 MCP `baidu-maps` | 推荐 | 兜底 / 大牌抽检 |
| Python + Pillow | 可选 | EXIF GPS：`scripts/parse_image_location.py` |

高德 / 百度需自行配置 API Key 与（百度）IP 白名单。

---

## 仓库结构

```
nengzuoma-yongge/
├── SKILL.md                 # Skill 入口
├── README.md
├── LICENSE
├── references/
│   ├── yongge-decision-core.md   # 红线 / 选址 / 案例锚点
│   ├── street-score-auto.md      # 可自动打分项
│   ├── category-fit-matrix.md    # 位置 × 业态
│   └── output-template.md        # 输出与语气
└── scripts/
    └── parse_image_location.py
```

---

## 设计原则

1. **勇哥规则是唯一大脑**；地图与看图只供血。  
2. **默认劝退**；绿只表示「未触红线且匹配」，仍要蹲点。  
3. **双地图不默认全量交叉**（数据同类、坐标系不同）；百度用于兜底与关键抽检。  
4. **与「勇哥」本人及原机构无官方关联**；方法论整理自公开信息。

母体方法论与案例库可参考社区整理：  
[Astro-wen/yongge-restaurant-skill](https://github.com/Astro-wen/yongge-restaurant-skill)（非本仓库官方关联）。

---

## 免责声明

- 决策辅助，**非**投资、法律、会计建议。  
- 地图 POI ≠ 真实客流；绿灯仍须现场蹲点与证照排查。  
- 案例与品牌评价基于公开信息与规则推断，不构成对任何主体的指控。  
- 最终经营责任由使用者本人承担。

---

## License

MIT · 见 [LICENSE](./LICENSE)

---

**能做吗？勇哥。不能做的，别硬开。**
