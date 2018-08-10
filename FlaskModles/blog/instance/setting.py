# -*- coding:utf-8 -*-
'''
项目的配置文件，配置的key必须为大写字母
'''
# 是否开启调试模式
DEBUG = True

# session必须要设置key
SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# mysql数据库连接信息,mysql+mysqlconnector(解决  Warning: (1366, "Incorrect string value: '\xD6\xD0\xB9\xFA\xB1\xEA.)
# https://segmentfault.com/a/1190000010596306
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456@localhost:3306/blog_db'

SQLALCHEMY_COMMIT_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True