# -*- coding:utf-8 -*-

'''
与用户认证相关的蓝本
'''

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
