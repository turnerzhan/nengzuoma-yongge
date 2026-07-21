# 为啥 Google 搜不到？能不能解决？

## 直接结论

| 问题 | 答案 |
|------|------|
| 网站挂了吗？ | **没有**，Pages 返回 200 |
| 验证成功了吗？ | **成功**（Search Console） |
| Google 收录了吗？ | **多数时候还没有**（验证 ≠ 收录） |
| 能「立刻」上首页吗？ | **不能保证**，没有人能强制 Google 秒收录 |
| 我们能做什么？ | 去掉技术障碍 + 主动提交 + 外链，**加快**收录 |

## 真正原因（不是玄学）

1. **新站空窗期**  
   从验证到出现在 `site:` 搜索，常见 **3～14 天**，冷门站更长。

2. **验证 ≠ 索引**  
   Search Console 绿勾只证明「域名/前缀归你」。  
   还要：**抓取 → 编入索引 → 排序**。后两步是 Google 的队列。

3. **关键词被占**  
   「能做吗？勇哥」= 海量网红内容。  
   即使收录了，搜这四个字也**很难**压过抖音/知乎。  
   应推：`nengzuoma-yongge`、`能做吗勇哥 github`。

4. **几乎没有外链**  
   Google 更爱爬「被别人链接」的站。只躺在 GitHub 上会很慢。

## 已做的技术修复（本仓库）

- `docs/robots.txt` — 允许抓取  
- `docs/sitemap.xml` — 站点地图  
- `docs/about.html` — 可索引长文介绍（利于「能做吗勇哥是什么」）  
- `docs/llms.txt` — Pages 可访问（以前根目录 llms 在 Pages 上 404）  
- 首页 `index,follow` + 正确 canonical / JSON-LD  

## 你必须点的（否则仍慢）

### A. Search Console（今天）

1. 打开已验证的资源：`https://turnerzhan.github.io/nengzuoma-yongge/`  
2. **Sitemaps** → 提交：

   ```text
   https://turnerzhan.github.io/nengzuoma-yongge/sitemap.xml
   ```

3. **网址检查** → 逐个 **请求编入索引**：

   ```text
   https://turnerzhan.github.io/nengzuoma-yongge/
   https://turnerzhan.github.io/nengzuoma-yongge/about.html
   https://turnerzhan.github.io/nengzuoma-yongge/index.html
   ```

### B. 外链（今天～本周，最有效）

发 3 条带**完整 https 链接**的帖（朋友圈 / 小红书 / 即刻 / 语雀），文案见 `LAUNCH_POST.md`。

### C. 正确搜索方式（验收）

```text
site:turnerzhan.github.io/nengzuoma-yongge
"nengzuoma-yongge"
能做吗勇哥 github
```

**不要用**「能做吗？勇哥」当验收标准——那是网红词红海。

## 现实预期

| 时间 | 可能状态 |
|------|----------|
| 0～3 天 | 仍 `site:` 为空，正常 |
| 3～14 天 | Pages 开始出现在 `site:` |
| 2～8 周 | `nengzuoma-yongge` 可被普通搜索找到 |
| 长期 | 「能做吗勇哥」仍可能排在网红后面，需持续外链与内容 |

## 一句话

> **不是坏了，是 Google 还没把你放进公开索引。**  
> 技术障碍我们能清；**秒搜到全世界**做不到。  
> 提交 sitemap + 请求索引 + 发外链 = 目前唯一正经解法。
