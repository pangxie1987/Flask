# -*- coding:utf-8 -*-
'''
项目初始化文件
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# 创建项目对象
app = Flask(__name__)

# # 实例化文件夹，instance_relative_config=True 则从../instance/setting.py中加载配置
# app = Flask(__name__, instance_relative_config=True)


# 加载配置文件内容
app.config.from_object('blog.setting') #模块下的setting文件名，不需要加.py后缀
app.config.from_pyfile('setting.py')    #从py文件中导入配置
app.config.from_envvar('FLASKR_SETTINGS') #环境变量，指向配置文件setting的路径
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost:3306/blog_db?charset=utf8'

# 创建数据库对象
db = SQLAlchemy(app)

from blog.model.User import User
from blog.model.Category import Category
from blog.controller import blog_message

# 登录管理
# 声明login对象
login_manager = LoginManager()

# 初始化绑到到应用
login_manager.init_app(app)

# 声明默认视图为login，当我们进行@require_login时，如果没有登录会自动跳转到该视图函数处理
login_manager.login_view = 'login'

# 当登录成功后，该函数会自动从会话中存储的用户ID重新加载用户对象。它应该接受一个用户的Unicode ID作为参数，并且返回相应的用户对象
@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))