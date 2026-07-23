# Changelog

## 1.6.0 — 2026-07-24

- **产品收口为三件事：**  
  1）核心对齐 `yongge-zuobuliao` 最新决策核/流程快照  
  2）连麦日账表必给咨询者  
  3）高德+百度 MCP **双通道永久保留**（竞品/客流源/交通等）；单环境 Key 失败只降级不拆通道  
- 从本机 yongge-zuobuliao 覆盖同步 decision-core / matrix / street-score  
- `SKILL.md` 简化；恢复 ponytail 误删的 references / profit_model / architecture
## 1.5.1 — 2026-07-24

- **完整回滚 ponytail 伤及 skill 的部分**（对照 `c5aa5e3^`）  
  - 恢复：`references/*` 决策核全套、`tools/profit_model.py`、`docs/architecture/*`  
  - **不回滚**（属合理瘦身）：SEO 文案堆、双份 `scripts/`、多余关键词落地页  
- 两刀说明：第一刀误伤决策核；第二刀仅 Pages 着陆页

## 1.5.0 — 2026-07-24

- **恢复 ponytail 误删决策核**：`references/yongge-decision-core` · `category-fit-matrix` · `street-score-auto` · `profit-model`
- 纠正「短句=少话」：连麦目标 1200～2500 字讲透；必加载 references + `corpus/06`
- 规定：以后瘦身禁止砍决策核/金句池

## 1.4.1 — 2026-07-24

- **纠偏灵魂**：输出模板改为「台上连麦语流 + 台下自检」；禁止 `### 1.为什么` 标题墙对客
- 学 zuobuliao 的短/狠/有数，不学其报告壳；账表仍为唯一锁定正式表

## 1.4.0 — 2026-07-24

- **固化** `skill/输出模板.md`：连麦账表行项目不可改 + 对齐 yongge-zuobuliao 输出骨架
- 口吻/格式权威：zuobuliao `output-template`；账表权威：直播 Excel
- `SKILL.md` 1.4.0：输出权威表、必读顺序、自检绑定模板

## 1.3.1 — 2026-07-24

- **连麦账表**：对齐勇哥桌面 Excel「这家餐饮店能救吗？」
- 默认按天：营业额/毛利率/毛利/房租/人工/水电/固定成本/保本线/纯利；现状 vs 调整后
- `breakeven.py run` 增加 `lianmai_board`；风格/保本线文档同步

## 1.3.0 — 2026-07-24

- **连麦默认闸门**：`SKILL.md` 产品终点 + `yongge`/`brief` 双模式
- `skill/风格指引.md`：共情定义、小账表规则、脏话边界、防尽调自检
- 专业能力台下算；台上给人话结论（能不能做 / 有没有坑）

## 1.2.0 — 2026-07-24

- **ponytail 瘦身**：删除 `scripts/` 双份、SEO 文档堆、references 正文、architecture、海报 HTML、CITATION
- 工具统一：`tools/breakeven.py` 支持 run/plan/iron（兼容旧无参）
- 发布说明合并为 `docs/PUBLISH.md`；sitemap 精简

## 1.1.0 — 2026-07-21

- SEO/GEO 包装、Pages、Release、原创产品叙事

## 1.0.0 — 2026-07-21

- 完整知识库 corpus/cases/skill/tools
