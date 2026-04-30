# 个人博客操作指南

> 基于 Flask + Markdown 的漫威风格个人博客
![效果展示](./images/效果图.png)
---

## 目录

1. [项目结构](#1-项目结构)
2. [安装依赖](#2-安装依赖)
3. [本地运行](#3-本地运行)
4. [宝塔面板部署](#4-宝塔面板部署)
5. [文章写作](#5-文章写作)
6. [图片上传](#6-图片上传)
7. [自定义配置](#7-自定义配置)
8. [常见问题](#8-常见问题)

---

## 1. 项目结构

```
ceshi02/
├── app.py              # Flask 应用主程序
├── wsgi.py             # WSGI 入口文件（用于生产环境）
├── requirements.txt    # Python 依赖列表
├── .user.ini           # PHP 配置（已保留）
├── posts/              # 文章目录（Markdown 文件）
│   ├── marvel-and-code.md
│   ├── flask-quickstart.md
│   └── markdown-guide.md
├── templates/          # HTML 模板
│   ├── base.html       # 基础模板
│   ├── index.html      # 首页
│   ├── post.html       # 文章详情页
│   ├── archives.html   # 档案页
│   ├── categories.html # 分类页
│   ├── tags.html       # 标签页
│   ├── about.html      # 关于/简历页
│   └── 404.html        # 404 错误页
├── static/             # 静态资源
│   ├── css/
│   │   └── style.css   # 漫威风格样式
│   ├── js/
│   │   └── main.js     # JavaScript
│   └── uploads/        # 上传的图片目录
└── 操作指南.md          # 本文档
```

---

## 2. 安装依赖

### 前置要求

- Python 3.8 或更高版本
- pip 包管理器

### 安装步骤

```bash
# 进入项目目录
cd d:\wwwroot\ceshi02

# 安装依赖（推荐使用虚拟环境）
python -m venv venv

# 激活虚拟环境（Windows）
venv\Scripts\activate

# 安装依赖包
pip install -r requirements.txt
```

**requirements.txt 内容：**

```
Flask==3.0.0
Flask==3.0.0
Markdown==3.5.1
PyYAML==6.0.1
gunicorn==21.2.0
Pygments==2.17.2
```

---

## 3. 本地运行

### 开发模式

```bash
# 确保虚拟环境已激活
python app.py
```

访问 `http://127.0.0.1:5000` 即可查看博客。

### 热重载

Flask 默认开启了 debug 模式，修改代码后会自动重载服务器。

---

## 4. 宝塔面板部署

> 本节专为初次在宝塔面板部署 Python 项目的新手编写，每一步都有详细说明。
>
> **部署配置**
> - 域名：`www.example.com`
> - 服务器IP：`192.168.1.100`
> - 宝塔面板：`http://192.168.1.100:8888`

### 4.1 部署前准备

#### 4.1.1 检查本地环境

在本地确保已经安装并测试通过：

```bash
# 进入项目目录
cd d:\wwwroot\ceshi02

# 创建虚拟环境（可选，仅本地测试用）
python -m venv venv
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 本地测试运行
python app.py
```

确认本地访问 `http://127.0.0.1:5000` 正常后，按 `Ctrl+C` 停止本地服务器。

#### 4.1.2 打包项目文件

将以下文件/文件夹**全部**选中并压缩为 ZIP 文件：

```
ceshi02/
├── app.py
├── wsgi.py
├── requirements.txt
├── posts/
├── templates/
├── static/
└── .user.ini
```

> 注意：不要压缩整个 ceshi02 文件夹，而是压缩里面的内容。

---

### 4.2 登录宝塔面板

1. 打开浏览器，访问宝塔面板地址：`http://192.168.1.100:8888`
2. 使用管理员账号登录
3. 进入面板主界面

---

### 4.3 安装 Python 项目管理器插件

> 如果已经安装过，请跳过此步骤。

#### 4.3.1 在线安装

1. 在宝塔面板左侧栏点击 **软件商店**
2. 在搜索框输入 **Python 项目管理器**
3. 点击 **安装**
4. 等待安装完成（通常需要 1-2 分钟）

#### 4.3.2 离线安装（可选）

如果在线安装失败：
1. 点击 **软件商店** -> **离线安装**
2. 上传宝塔提供的 Python 管理器离线包
3. 按提示完成安装

---

### 4.4 创建网站

#### 4.4.1 添加站点

1. 在宝塔面板左侧点击 **网站**
2. 点击 **添加站点**
3. 填写配置：

| 配置项 | 示例值 | 说明 |
|--------|--------|------|
| 域名 | `www.example.com` | 你的域名 |
| 根目录 | `/www/wwwroot/example.com` | 网站根目录 |
| FTP | 不创建 | 新手建议跳过 |
| 数据库 | 不创建 | 本项目不需要 MySQL |
| PHP | 不设置 | 不需要 PHP |

4. 点击 **提交**

#### 4.4.2 上传项目文件

1. 点击站点右侧的 **根目录** 按钮，进入文件管理器
2. 删除自动生成的默认文件（如有）
3. 点击 **上传**
4. 上传之前准备好的 ZIP 文件
5. 上传完成后，右键解压文件
6. 确保解压后的文件结构正确：

```
www/wwwroot/example.com/
├── app.py
├── wsgi.py
├── requirements.txt
├── posts/
├── templates/
├── static/
└── .user.ini
```

---

### 4.5 配置 Python 项目

#### 4.5.1 添加 Python 项目

1. 在宝塔面板左侧找到 **Python 项目管理器**（如果没看到，刷新页面）
2. 点击 **添加项目**
3. 填写配置：

| 配置项 | 值 | 说明 |
|--------|-----|------|
| 项目名称 | `my_blog` | 任意名称 |
| 项目路径 | `/www/wwwroot/example.com` | 网站根目录 |
| 框架 | `Flask` | 选择 Flask |
| 启动文件 | `wsgi.py` | WSGI 入口 |
| 监听端口 | `5000` | Flask 默认端口 |
| 虚拟环境 | 选择 Python 版本 | 建议 Python 3.11 |

4. 点击 **提交**

#### 4.5.2 安装依赖

项目添加后，点击项目右侧的 **SSH 终端** 按钮，执行：

```bash
# 如果没有自动创建虚拟环境，先创建
python -m venv venv

# 激活虚拟环境（Linux 环境）
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

#### 4.5.3 测试运行

1. 在 Python 项目管理器中，点击项目右侧的 **启动** 按钮
2. 查看日志，确认无报错
3. 点击 **访问** 按钮或直接访问 `http://127.0.0.1:5000`

> 如果无法访问，检查防火墙是否开放 5000 端口（后续用 Nginx 代理后不需要）。

---

### 4.6 配置 Nginx 反向代理

> 通过 Nginx 代理到 80 端口，这样访问域名时不需要加端口号。

#### 4.6.1 修改站点配置

1. 在宝塔面板左侧点击 **网站**
1. 点击站点 `www.example.com` 右侧的 **设置**
3. 在弹出的窗口中点击 **反向代理**
4. 点击 **添加反向代理**
5. 配置：

| 配置项 | 值 |
|--------|-----|
| 代理名称 | `flask_app` |
| 代理类型 | `http` |
| 目标地址 | `http://127.0.0.1:5000` |
| 发送域名 | `$host` |

6. 点击 **提交**

#### 4.6.2 配置静态文件（重要！）

Nginx 默认不会代理静态文件，需要额外配置：

1. 在网站设置页面点击 **配置文件**
2. 在 `server` 块内添加静态文件配置：

```nginx
# 静态文件配置
location /static/ {
    alias /www/wwwroot/example.com/static/;
    expires 30d;
}

# 上传的图片目录
location /static/uploads/ {
    alias /www/wwwroot/example.com/static/uploads/;
    expires 30d;
}
```

3. 点击 **保存** 并重启 Nginx

---

### 4.7 域名与 SSL 配置

#### 4.7.1 解析域名

你的域名 `www.example.com` 已解析到服务器 `192.168.1.100`。

验证解析是否生效：
```bash
ping www.example.com
# 应该显示 192.168.1.100
```

> 如果尚未解析，在阿里云控制台添加A记录：
> - 记录类型：A
> - 主机记录：www
> - 记录值：192.168.1.100

#### 4.7.2 申请 SSL 证书（免费）

1. 在网站设置页面点击 **SSL**
2. 点击 **Let's Encrypt** 免费证书
3. 点击 **申请** -> **确认**
4. 申请成功后，打开 **强制 HTTPS** 开关
5. 点击 **保存**

---

### 4.8 验证部署

完成以上步骤后，在浏览器中访问 `https://www.example.com`，应该能看到博客首页。

**检查要点：**
- [ ] 域名可以访问（显示博客首页）
- [ ] 导航栏链接可以点击
- [ ] 文章列表正常显示
- [ ] 图片正常加载
- [ ] HTTPS 生效（有锁图标）

---

### 4.9 部署检查清单

```
□ 1. 项目文件已上传并解压到 /www/wwwroot/example.com
□ 2. Python 项目管理器中项目已添加并启动
□ 3. 依赖已安装（pip install -r requirements.txt 成功）
□ 4. 反向代理已配置（目标：http://127.0.0.1:5000）
□ 5. 静态文件路径已配置（/www/wwwroot/example.com/static/）
□ 6. 域名 www.example.com 已解析到 192.168.1.100
□ 7. SSL 证书已申请并强制 HTTPS
□ 8. 可以在浏览器中正常访问 https://www.example.com
```

---

### 4.10 日常维护

#### 重启项目

如果修改了代码需要重启：

1. 在 Python 项目管理器中找到项目
2. 先点击 **停止**，再点击 **启动**
3. 或者直接点击 **重启**

#### 查看日志

1. 在 Python 项目管理器中点击项目右侧的 **日志**
2. 查看运行日志排查问题

#### 备份

定期备份以下文件：
- `posts/` 目录（所有文章）
- `templates/` 目录（如果修改过模板）
- `static/` 目录（如果修改过样式或上传了图片）

---

## 5. 文章写作

### 5.1 创建新文章

在 `posts/` 目录下创建一个 `.md` 文件，文件名即为文章标识。

### 5.2 文章格式

每个文章文件开头需要包含 YAML front matter：

```markdown
---
title: "文章标题"
slug: article-slug        # URL 标识，唯一
date: "2026-04-20"        # 日期
category: "分类"           # 分类名称
tags: ["标签1", "标签2"]  # 标签列表
summary: "文章摘要..."    # 摘要，用于列表页显示
cover: ""                  # 封面图 URL（可选）
---

这里是文章的正文内容，使用 Markdown 格式编写。
```

### 5.3 示例

```markdown
---
title: "我的第一篇文章"
slug: my-first-post
date: "2026-04-20"
category: "教程"
tags: ["Python", "Flask"]
summary: "这是我的第一篇技术博客文章，介绍如何使用 Flask 框架。"
---

## 正文开始

这里使用 Markdown 语法编写正文内容。

### 二级标题

- 列表项 1
- 列表项 2

### 代码示例

```python
print("Hello, World!")
```

### 插入图片

![图片描述](./images/example.jpg)

> 注意：相对路径的图片会自动转换为静态文件路径
```

### 5.4 插入图片

在 Markdown 中使用相对路径引用图片：

```markdown
![图片描述](./images/photo.jpg)
```

图片文件放在 `static/uploads/` 目录下，建议按年月分类：

```
static/uploads/
├── 2026-04/
│   ├── photo1.jpg
│   └── photo2.png
└── 2026-05/
    └── banner.png
```

---

## 6. 图片上传

### 6.1 方式一：通过 Markdown 引用

将图片放入 `static/uploads/` 目录，在文章中引用：

```markdown
![风景图](./2026-04/landscape.jpg)
```

### 6.2 方式二：使用外部图片 URL

```markdown
![图片描述](https://example.com/image.jpg)
```

### 6.3 方式三：通过 FTP/SMB 上传

使用宝塔面板的文件管理或 FTP 工具，将图片上传到 `static/uploads/` 目录。

### 6.4 推荐目录结构

```
static/uploads/
├── 2026-04/
│   ├── article-covers/     # 文章封面图
│   └── article-images/     # 文章内嵌图片
└── 2026-05/
    └── ...
```

---

## 7. 自定义配置

### 7.1 修改个人信息

编辑 `templates/about.html` 修改简历页的个人信息：

- 头像图标：修改 `<i class="fas fa-user-astronaut">`
- 姓名：在 `about-avatar-name` 中修改
- 职位：在 `about-avatar-title` 中修改
- 自我介绍：修改 `<p>` 标签内容
- 技术栈：修改 `skills-grid` 中的技能项
- 经历：修改 `timeline` 中的时间线

### 7.2 修改博客名称

在 `templates/base.html` 中修改：

- 导航栏 Logo 文字
- 页脚 Logo 文字
- 首页标题

### 7.3 修改样式

编辑 `static/css/style.css` 自定义样式：

```css
:root {
    --primary: #E23636;      /* 主题红色 */
    --accent: #FFD700;       /* 强调金色 */
    --dark-bg: #0A0A0F;      /* 背景色 */
    /* ... 更多变量 */
}
```

### 7.4 添加社交链接

在 `templates/base.html` 的 `footer-social` 部分添加：

```html
<a href="你的GitHub链接"><i class="fab fa-github"></i></a>
<a href="你的Twitter链接"><i class="fab fa-twitter"></i></a>
```

---

## 8. 常见问题

### Q1: 页面显示 404？

- 确保 `posts/` 目录下有 `.md` 文件
- 检查 front matter 中的 `slug` 是否唯一
- 重启 Flask 应用

### Q2: 图片不显示？

- 确保图片放在 `static/uploads/` 目录
- 检查图片路径是否正确
- 确认 Nginx 静态文件配置

### Q3: 中文显示乱码？

- 确保所有文件使用 UTF-8 编码
- Markdown 文件保存时选择 UTF-8 编码

### Q4: 如何升级依赖？

```bash
pip install --upgrade -r requirements.txt
```

### Q5: 如何备份文章？

只需备份 `posts/` 目录即可，其他文件可从 Git 重新获取。

### Q6: 支持评论功能吗？

当前版本不包含评论功能。如需添加，可考虑使用：
- Disqus
- Gitalk
- Valine

### Q7: 宝塔面板中 Python 项目启动失败？

1. 在 Python 项目管理器中点击 **日志** 查看具体报错
2. 常见错误：
   - **端口被占用**：更换端口（如改为 5001）
   - **依赖缺失**：在 SSH 终端中执行 `pip install -r requirements.txt`
   - **路径错误**：检查项目路径是否正确指向 `/www/wwwroot/ceshi02`
   - **venv 未创建**：先在项目设置中创建虚拟环境

### Q8: 502 Bad Gateway 错误？

这是 Nginx 无法连接到 Python 服务，检查：
1. Python 项目是否处于 **已启动** 状态
2. 监听端口是否与配置一致（默认 5000）
3. 防火墙是否放行了对应端口（命令：`ufw allow 5000`）
4. Nginx 反向代理的 **目标地址** 是否填写正确（`http://127.0.0.1:5000`）

### Q9: 静态文件（CSS/JS/图片）加载失败？

1. 确认 `static/` 目录已上传到服务器
2. 检查 Nginx 配置中是否有静态文件路径
3. 确认文件权限：`chmod -R 755 /www/wwwroot/ceshi02/static`
4. 重启 Nginx：在宝塔面板中点击 Nginx -> 重启

### Q10: 修改代码后需要重启吗？

是的！Python 项目不像 PHP 那样自动重载，必须手动重启：
1. Python 项目管理器 -> 停止 -> 启动
2. 或直接点击 **重启** 按钮

### Q11: 如何修改博客的 Logo 和名称？

编辑 `templates/base.html`，找到以下位置修改：
- 导航栏：`HERO'S LOG` 文字
- 页脚：`<span>HERO'S LOG</span>` 文字
- 浏览器标签页标题：修改 `<title>` 标签

### Q12: 如何绑定自己的域名？

1. 在阿里云云解析 DNS 中添加 A 记录指向服务器公网 IP
2. 在宝塔面板中添加站点，填入你的域名
3. 按本文档配置反向代理和 SSL
4. 等待 DNS 生效（通常 10 分钟-24 小时）
- Valine

---

## 联系方式

如有问题，请在项目 Issue 中反馈。

---

*最后更新：2026年4月*
