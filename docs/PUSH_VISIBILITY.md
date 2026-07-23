# 公开搜索可见 · 7 日作战计划

目标：**让陌生人能通过搜索找到「能做吗？勇哥 / nengzuoma-yongge」**。

> 现实约束：没人能保证 Google「今天搜就能上首页」。  
> 能保证的是：技术可抓取 + 主动提交 + 外链密度 → **最快进入索引**。

---

## 0. 当前状态（每次推前先认清）

| 项 | 状态 |
|----|------|
| 网站可访问 | ✅ Pages 200 |
| Search Console 验证 | ✅（你已完成） |
| Google 公开索引 | ❌ 或极慢（`site:` 常仍为空） |
| 主推荐搜索词 | `nengzuoma-yongge` · `能做吗勇哥 github` |

**验收标准（成功定义）：**

```text
site:turnerzhan.github.io/nengzuoma-yongge
```

出现 ≥1 条 = **公开可见（第一阶段成功）**。  
不要用「能做吗？勇哥」四个字当验收——网红词会永远压你。

---

## 1. 规范对外三件套（所有渠道统一）

复制即用：

```text
【能做吗？勇哥】开源开店验铺 Agent Skill
英文：NengZuoMa YongGe
ID：nengzuoma-yongge
GitHub：https://github.com/turnerzhan/nengzuoma-yongge
介绍页：https://turnerzhan.github.io/nengzuoma-yongge/
详细介绍：https://turnerzhan.github.io/nengzuoma-yongge/about.html
```

**禁止**只写「搜能做吗勇哥」不带链接。

---

## 2. 第 0 天：Search Console 必点（30 分钟）

打开：https://search.google.com/search-console

### 2.1 提交 Sitemap

资源：`https://turnerzhan.github.io/nengzuoma-yongge/`  
→ **Sitemaps** → 新增：

```text
https://turnerzhan.github.io/nengzuoma-yongge/sitemap.xml
```

状态应变为「成功」或「已发现」。

### 2.2 请求编入索引（逐条）

**网址检查** → 粘贴 → **请求编入索引**：

1. `https://turnerzhan.github.io/nengzuoma-yongge/`  
2. `https://turnerzhan.github.io/nengzuoma-yongge/about.html`  
3. `https://turnerzhan.github.io/nengzuoma-yongge/canyinxuanzhi.html`  
4. `https://turnerzhan.github.io/nengzuoma-yongge/jiamengbikeng.html`  

每天配额有限，优先 1、2。

### 2.3 看「覆盖率 / 网页索引」

- 已编入索引 > 0 → 第一阶段完成  
- 仍是 0 → 继续外链，3 天后再请求一次首页  

---

## 3. 第 0 天：必应 + 国内（比 Google 往往更快）

### 3.1 Bing Webmaster

1. https://www.bing.com/webmasters  
2. 添加：`https://turnerzhan.github.io/nengzuoma-yongge/`  
3. 用 XML 文件或 meta 验证（同 Google，可再下验证文件放到 `docs/`）  
4. 提交 sitemap 同上  
5. URL 提交工具批量提交 4 个页面  

> 仓库已接过 IndexNow；Bing 常比 Google 先露脸。

### 3.2 百度（中文用户更关键）

1. https://ziyuan.baidu.com  
2. 添加站点：`https://turnerzhan.github.io/nengzuoma-yongge/`  
3. 验证后提交 sitemap  
4. 普通收录 + 链接提交  

国内用户很多**不用 Google**——百度可见往往比 Google 更实在。

---

## 4. 第 1～3 天：外链爆发（最有效）

每天至少 **2 条带完整 https 链接** 的公开内容：

| 日 | 渠道 | 做什么 |
|----|------|--------|
| D1 | 朋友圈 + 微信群 | 用 `LAUNCH_POST.md` 短文，贴双链 |
| D1 | 小红书 | 标题含「能做吗勇哥」「nengzuoma-yongge」 |
| D2 | 即刻 / V2EX | 产品向发帖 |
| D2 | 语雀 / 飞书文档公开 | 长文 + 锚链 GitHub |
| D3 | 公众号 / 知乎回答 | 「开店如何选址」类问题下回答并链项目 |
| D3 | 朋友二次转发 | 求 3 个朋友转发带链接 |

文案模板：仓库内 `docs/LAUNCH_POST.md`。

**规则：**

- 正文必须出现可点击的 `https://`  
- 至少提一次 **`nengzuoma-yongge`**  
- 不要只发图不发链  

---

## 5. 第 4～7 天：验收与加码

### 5.1 每天搜一次

```text
site:turnerzhan.github.io/nengzuoma-yongge
site:github.com/turnerzhan/nengzuoma-yongge
"nengzuoma-yongge"
```

### 5.2 Search Console 看数据

- 抓取 → 是否已抓取  
- 网页索引 → 已编入数量  
- 效果 → 有没有展示（有展示但点击少再优化标题）

### 5.3 若 7 天仍 site 为空

1. 再请求索引首页 + about  
2. 再发 3 条外链（换平台）  
3. 检查验证文件仍在：  
   `https://turnerzhan.github.io/nengzuoma-yongge/google9f44dcc4b6d9096d.html`  
4. 不要反复改域名/改项目名（伤收录）

---

## 6. 搜索词策略（对外怎么教别人找）

| 优先级 | 教用户搜 | 预期 |
|--------|----------|------|
| P0 | `nengzuoma-yongge` | 收录后最稳 |
| P0 | `能做吗勇哥 github` | 中文+场景 |
| P1 | `NengZuoMa YongGe` | 英文 |
| P1 | `餐饮选址 Agent Skill` | 长尾 |
| P2 | `能做吗？勇哥` | 难，被网红占 |

传播时主动说：

> 搜 **nengzuoma-yongge**，或打开下面链接……

---

## 7. 技术侧已具备（无需你再改代码也能推）

- Pages 首页 / about / 关键词页  
- robots.txt · sitemap.xml  
- Google 验证文件  
- IndexNow（Bing）  
- Release v1.1.0  

推的重点从「再改仓库」转为 **提交 + 外链**。

---

## 8. 一页检查清单（打印）

- [ ] GSC 已验证 Pages  
- [ ] Sitemap 已提交且成功  
- [ ] 首页 + about 已「请求编入索引」  
- [ ] Bing 已添加并提交  
- [ ] 百度资源已添加（可选但推荐）  
- [ ] 今天发出 ≥2 条带完整链接的公开内容  
- [ ] 本周累计 ≥8 条外链曝光  
- [ ] 验证文件未删除  
- [ ] 对外统一使用三件套文案  

---

## 9. 成功后的下一步（第二阶段）

`site:` 有结果之后：

1. 看 GSC「效果」里实际搜索词，反写小红书标题  
2. 每周 1 篇长尾文（加盟避坑案例、保本线怎么算）链回项目  
3. 不要改仓库名、不要频繁换域名  

---

**一句话：**  
公开搜索可见 = **索引 + 外链**；  
今天把 GSC sitemap/请求索引点完，并按 D1～D3 发链接，是整条链路里 ROI 最高的动作。
