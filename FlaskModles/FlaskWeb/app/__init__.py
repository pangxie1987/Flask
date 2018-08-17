# -*- coding:utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap(app)
# 初始化数据库
db = SQLAlchemy(app)
# 时间戳
moment = Moment(app)
# 数据库迁移框架
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

from app import views

