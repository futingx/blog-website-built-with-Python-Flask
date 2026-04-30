import os
from app import app

# 关闭 Flask debug 模式（生产环境必需）
os.environ.setdefault('FLASK_ENV', 'production')

# Gunicorn 配置（用于宝塔面板部署）
bind = '127.0.0.1:5000'
workers = 2
threads = 2
timeout = 120
accesslog = '-'
errorlog = '-'
loglevel = 'info'

if __name__ == '__main__':
    app.run()
