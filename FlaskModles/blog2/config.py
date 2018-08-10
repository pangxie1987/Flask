# -*- coding:utf-8 -*-
'''
数据库连接配置
'''
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(basedir, 'app.db')  # 是the Flask-SQLAlchemy必需的扩展。这是我们的数据库文件的路径
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')  # 是用来存储SQLAlchemy-migrate数据库文件的文件夹。
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
print(basedir)