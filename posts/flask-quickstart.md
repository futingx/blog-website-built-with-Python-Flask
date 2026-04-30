---
title: "Flask 快速入门指南"
slug: flask-quickstart
date: "2026-04-15"
category: "教程"
tags: ["Python", "Flask", "Web开发"]
summary: "Flask 是一个轻量级的 Python Web 框架，非常适合快速构建小型到中型的 Web 应用。本文将带你快速上手 Flask 开发。"
cover: ""
---

## 什么是 Flask？

Flask 是一个使用 Python 编写的轻量级 Web 应用框架。它由 Armin Ronacher 开发，以其简洁、灵活的特点受到广大开发者喜爱。

## 安装 Flask

首先，确保你已安装 Python（建议 3.8+），然后使用 pip 安装 Flask：

```bash
pip install Flask
```

## 创建第一个 Flask 应用

创建一个名为 `app.py` 的文件：

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

运行应用：

```bash
python app.py
```

访问 `http://127.0.0.1:5000`，你就能看到 "Hello, World!" 了！

## 路由与视图函数

Flask 使用装饰器来定义路由：

```python
@app.route('/')
def index():
    return '这是首页'

@app.route('/about')
def about():
    return '这是关于页面'

@app.route('/user/<username>')
def user_profile(username):
    return f'欢迎，{username}！'
```

## 模板渲染

Flask 集成了 Jinja2 模板引擎。在 `templates` 文件夹中创建 HTML 文件：

```python
from flask import render_template

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)
```

## 处理表单数据

```python
from flask import request, render_template_string

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 验证用户...
        return f'欢迎，{username}！'
    return render_template('login.html')
```

## 数据库集成

Flask 可以与多种数据库配合使用，推荐使用 Flask-SQLAlchemy：

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Post {self.title}>'
```

## 总结

Flask 是学习 Web 开发的绝佳起点，它的轻量级设计让你能够专注于核心功能，而不是被复杂的配置所困扰。

| 特性 | 说明 |
|------|------|
| 路由系统 | 强大且易于使用 |
| 模板引擎 | Jinja2，功能丰富 |
| 扩展生态 | 丰富的插件支持 |
| 文档完善 | 官方文档详尽 |

---

更多内容，欢迎在我的博客中探索！
