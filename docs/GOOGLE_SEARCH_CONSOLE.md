# Google Search Console 收录指南 · 能做吗？勇哥

目标：让 Google **尽快知道并收录** 这两个地址：

1. https://github.com/turnerzhan/nengzuoma-yongge  
2. https://turnerzhan.github.io/nengzuoma-yongge/

> 收录 ≠ 搜「能做吗？勇哥」就排第一。  
> 中文品牌词仍会被网红内容占满；请同时推广 **`nengzuoma-yongge`**。

---

## 一、注册与登录

1. 打开：https://search.google.com/search-console  
2. 用 **Google 账号** 登录（建议用你常用、能收验证邮件的账号）  
3. 若提示「开始使用」，点进入控制台  

---

## 二、添加资源（做两次）

### 方式 A：网址前缀（推荐，简单）

对每个要收录的地址各添加一次：

#### ① GitHub 仓库

1. 点 **添加资源** → 选 **网址前缀**  
2. 填入（末尾建议带 `/` 也可不带，二选一保持一致即可）：

   ```text
   https://github.com/turnerzhan/nengzuoma-yongge
   ```

3. 验证方式：  
   - GitHub **无法** 方便地上传 HTML 文件到仓库根目录做 meta 验证（根目录可放，但 GitHub 不会当网站托管验证文件）  
   - **更现实**：用「HTML 标记」较难；GitHub 页面验证通常走 **域名资源** 不适合  
   - **实用方案**：优先验证 **GitHub Pages**（下面 ②），仓库靠外链与时间被爬；或使用「Google 已登录 + 你有该站关联」时的其它路径  

**说明：** GitHub.com 上的仓库页，个人往往 **无法完成 DNS/文件验证**（你不拥有 github.com 域名）。  
因此 **主推验证 Pages 子域**，仓库用发布与外链推动爬取。

#### ② GitHub Pages 落地页（务必做）

1. **添加资源** → **网址前缀**  
2. 填入：

   ```text
   https://turnerzhan.github.io/nengzuoma-yongge/
   ```

3. 验证方式推荐 **HTML 文件** 或 **HTML 标记**：

##### 方法 1：HTML 文件（推荐）

1. Search Console 会给你一个类似 `googleXXXXXXXX.html` 的文件  
2. 下载后，放到本仓库 **`docs/`** 目录下（与 `index.html` 同级）  
3. 提交并 push 到 `master`（Pages 源是 `/docs`）  
4. 浏览器打开确认能访问：  
   `https://turnerzhan.github.io/nengzuoma-yongge/googleXXXXXXXX.html`  
5. 回到 Search Console 点 **验证**  

##### 方法 2：HTML 标记

1. 复制 Search Console 给的 `<meta name="google-site-verification" content="..." />`  
2. 粘贴进 `docs/index.html` 的 `<head>` 里  
3. push 后验证  

---

## 三、请求编入索引（验证成功后立刻做）

对 **Pages** 资源：

1. 左侧 → **网址检查**（URL Inspection）  
2. 顶部输入：

   ```text
   https://turnerzhan.github.io/nengzuoma-yongge/
   ```

3. 等检查结束 → 点 **请求编入索引**  
4. 再对下面 URL 各请求一次：

   ```text
   https://turnerzhan.github.io/nengzuoma-yongge/index.html
   https://github.com/turnerzhan/nengzuoma-yongge
   https://github.com/turnerzhan/nengzuoma-yongge/releases/tag/v1.1.0
   https://raw.githubusercontent.com/turnerzhan/nengzuoma-yongge/master/llms.txt
   ```

> 每天请求次数有限，优先：Pages 首页 → 仓库首页 → Release。

---

## 四、加速被爬的额外动作

1. **发带链接的帖**（朋友圈/小红书/即刻/V2EX/即刻）  
   正文必须出现完整 `https://` 链接，不要只写「搜能做吗勇哥」。  
2. **语雀/公众号/博客** 发首发文（见同目录文案），锚链到 GitHub + Pages。  
3. 仓库 **Settings → Social preview** 上传 `docs/assets/cover-banner.jpg`。  
4. 等待 **3～14 天** 后，用下面命令自查是否收录。

---

## 五、如何自查是否已被 Google 收录

在 Google 搜索框输入：

```text
site:turnerzhan.github.io/nengzuoma-yongge
site:github.com/turnerzhan/nengzuoma-yongge
"nengzuoma-yongge"
"NengZuoMa YongGe"
"能做吗勇哥" site:github.com
```

- 有结果 → 已收录，可继续堆外链冲排名  
- 无结果 → 仍在排队，继续发外链 + 过几天再请求索引  

**不要指望：**

```text
能做吗？勇哥
```

短期能压过网红；应用：

```text
nengzuoma-yongge
能做吗勇哥 github
NengZuoMa 开店验铺
```

---

## 六、常见失败原因

| 现象 | 处理 |
|------|------|
| 验证文件 404 | 是否放在 `docs/` 且已 push；Pages 是否启用 |
| 请求索引灰掉 | 先完成资源验证 |
| 收录了但中文搜不到 | 正常；改推英文 ID + 「能做吗勇哥 github」 |
| Pages 一直 building | 等 10～30 分钟；检查 Settings → Pages 源为 master `/docs` |

---

## 七、本项目规范 URL（复制用）

```text
https://github.com/turnerzhan/nengzuoma-yongge
https://turnerzhan.github.io/nengzuoma-yongge/
https://github.com/turnerzhan/nengzuoma-yongge/releases/tag/v1.1.0
```
