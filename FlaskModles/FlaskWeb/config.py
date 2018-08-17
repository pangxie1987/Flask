# -*- coding:utf-8 -*-

import os, sys


CSRF_ENABLED = True # 激活 跨站点请求伪造 保护
SECRET_KEY = 'you-will-never-guess' # 加密令牌
# 数据库配置
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False