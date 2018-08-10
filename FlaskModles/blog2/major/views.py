# -*- coding:utf-8 -*-

from major import app

from models import User, ROLE_USER, ROLE_ADMIN

@app.route('/')
def index():
    return 'hello world, hello flask'