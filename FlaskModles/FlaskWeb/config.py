# -*- coding:utf-8 -*-

import os, sys

# CSRF_ENABLED = True # 激活 跨站点请求伪造 保护
# SECRET_KEY = 'you-will-never-guess' # 加密令牌
# # 数据库配置
# basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')    #数据库存储文件
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')    #数据库文件夹
# SQLALCHEMY_COMMIT_ON_TEARDOWN = True
# SQLALCHEMY_TRACK_MODIFICATIONS = False

# # 邮件服务配置
# MAIL_DEBUG = False             # 开启debug，便于调试看信息
# MAIL_SUPPRESS_SEND = False    # 发送邮件，为True则不发送
# MAIL_SERVER = 'smtp.163.com'   # 邮箱服务器
# MAIL_PORT = 25               # 端口
# #  'MAIL_USE_SSL' = True           # 163邮箱不需要
# #  'MAIL_USE_TLS' = False          # 不需要使用TLS
# MAIL_USERNAME = 'm18516292278@163.com'  # 填邮箱
# MAIL_PASSWORD = 'lpb123456'      # 填授权码
# MAIL_DEFAULT_SENDER = 'm18516292278@163.com'  # 填邮箱，默认发送者
# recipients = ['m18516292278@163.com', 'm18516292278@163.com']

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')    #数据库文件夹
# SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'app.sqlite')   #数据库存储文件
class Config:
    CSRF_ENABLED = True # 激活 跨站点请求伪造 保护
    SECRET_KEY = 'reset' # 加密令牌
    # 数据库配置   
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 邮件服务配置
    MAIL_DEBUG = False             # 开启debug，便于调试看信息
    MAIL_SUPPRESS_SEND = False    # 发送邮件，为True则不发送
    MAIL_SERVER = 'smtp.163.com'   # 邮箱服务器
    MAIL_PORT = 25               # 端口
    #  'MAIL_USE_SSL' = True           # 163邮箱不需要
    #  'MAIL_USE_TLS' = False          # 不需要使用TLS
    MAIL_USERNAME = 'm18516292278@163.com'  # 填邮箱
    MAIL_PASSWORD = 'lpb123456'      # 填授权码
    MAIL_DEFAULT_SENDER = 'm18516292278@163.com'  # 填邮箱，默认发送者
    recipients = ['m18516292278@163.com', 'm18516292278@163.com']
    RECEVIERS = ['m18516292278@163.com', 'm18516292278@163.com']
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_ADMIN = 'FLASK'
    FLASKY_POSTS_PER_PAGE = 6
    FLASKY_FOLLOWERS_PER_PAGE = 50
    

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app-dev.sqlite')   #数据库存储文件

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app-test.sqlite')    #数据库存储文件
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app-test.sqlite')    #数据库存储文件

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        #把错误通过电子邮件发送给管理员
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
                        mailhost = (cls.MAIL_SERVER, cls.MAIL_PORT),
                        fromaddr = cls.MAIL_DEFAULT_SENDER,
                        toaddrs = [cls.FLASK_ADMIN],
                        subject = cls.FLASKY_MAIL_SUBJECT_PREFIX + 'Application Error',
                        secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}