"""
Marvel-themed Personal Blog
基于 Flask 的个人博客系统，使用 Markdown 文件作为文章存储
"""

import os
import re
import yaml
import markdown
from datetime import datetime
from flask import Flask, render_template, abort, send_from_directory, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
app.config['POSTS_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'posts')

# 确保必要目录存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['POSTS_FOLDER'], exist_ok=True)


def parse_post(filepath):
    """解析 Markdown 文件，提取 YAML front matter 和正文"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 解析 YAML front matter
    meta = {}
    body = content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                meta = {}
            body = parts[2].strip()

    # 处理图片路径：将相对路径转换为 /static/uploads/ 路径
    # 匹配 markdown 图片语法，排除 http 开头的外部链接
    def replace_image_path(match):
        alt = match.group(1)
        path = match.group(2)
        # 去除开头的 ./，保持路径干净
        clean_path = path.lstrip('./')
        return f'![{alt}](/static/uploads/{clean_path})'
    body = re.sub(r'!\[([^\]]*)\]\((?!http)([^)]+)\)', replace_image_path, body)

    # 转换 Markdown 为 HTML
    md = markdown.Markdown(extensions=[
        'markdown.extensions.fenced_code',
        'markdown.extensions.codehilite',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
        'markdown.extensions.meta',
        'markdown.extensions.attr_list',
    ])
    html_content = md.convert(body)

    # 提取元数据
    filename = os.path.basename(filepath).replace('.md', '')
    post = {
        'slug': meta.get('slug', filename),
        'title': meta.get('title', filename),
        'date': meta.get('date', datetime.now().strftime('%Y-%m-%d')),
        'category': meta.get('category', '未分类'),
        'tags': meta.get('tags', []),
        'cover': meta.get('cover', ''),
        'summary': meta.get('summary', ''),
        'content': html_content,
        'filename': filename,
    }

    # 确保 tags 是列表
    if isinstance(post['tags'], str):
        post['tags'] = [t.strip() for t in post['tags'].split(',')]

    # 确保 date 是字符串
    if isinstance(post['date'], datetime):
        post['date'] = post['date'].strftime('%Y-%m-%d')

    return post


def get_all_posts():
    """获取所有文章，按日期倒序排列"""
    posts = []
    posts_dir = app.config['POSTS_FOLDER']
    if not os.path.exists(posts_dir):
        return posts

    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            try:
                post = parse_post(filepath)
                posts.append(post)
            except Exception as e:
                print(f"解析文章失败: {filename}, 错误: {e}")

    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts


def get_categories():
    """获取所有分类及其文章数量"""
    posts = get_all_posts()
    categories = {}
    for post in posts:
        cat = post['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(post)
    return categories


def get_tags():
    """获取所有标签及其文章数量"""
    posts = get_all_posts()
    tags = {}
    for post in posts:
        for tag in post['tags']:
            if tag not in tags:
                tags[tag] = []
            tags[tag].append(post)
    return tags


# ==================== 路由 ====================

@app.route('/')
def index():
    """主页"""
    posts = get_all_posts()
    categories_dict = get_categories()
    tags_dict = get_tags()
    return render_template('index.html', posts=posts, categories=categories_dict, tags=tags_dict)


@app.route('/post/<slug>')
def post_detail(slug):
    """文章详情页"""
    posts = get_all_posts()
    post = next((p for p in posts if p['slug'] == slug), None)
    if not post:
        abort(404)
    return render_template('post.html', post=post)


@app.route('/archives')
def archives():
    """档案页 - 按时间归档"""
    posts = get_all_posts()
    # 按年份分组
    archives_dict = {}
    for post in posts:
        year = post['date'][:4]
        if year not in archives_dict:
            archives_dict[year] = []
        archives_dict[year].append(post)
    # 按年份倒序
    sorted_archives = dict(sorted(archives_dict.items(), reverse=True))
    return render_template('archives.html', archives=sorted_archives)


@app.route('/categories')
def categories():
    """分类页"""
    cats = get_categories()
    return render_template('categories.html', categories=cats)


@app.route('/category/<name>')
def category_detail(name):
    """分类详情页"""
    cats = get_categories()
    posts = cats.get(name, [])
    return render_template('category_detail.html', category=name, posts=posts)


@app.route('/tags')
def tags():
    """标签页"""
    all_tags = get_tags()
    return render_template('tags.html', tags=all_tags)


@app.route('/tag/<name>')
def tag_detail(name):
    """标签详情页"""
    all_tags = get_tags()
    posts = all_tags.get(name, [])
    return render_template('tag_detail.html', tag=name, posts=posts)


@app.route('/about')
def about():
    """个人简历页"""
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    """404 页面"""
    return render_template('404.html'), 404


# 生产环境配置：关闭 DEBUG 模式
if os.environ.get('FLASK_ENV') == 'production':
    app.config['DEBUG'] = False

if __name__ == '__main__':
    # 本地开发使用，生产环境请使用 gunicorn
    app.run(debug=app.config.get('DEBUG', False), host='0.0.0.0', port=5000)
