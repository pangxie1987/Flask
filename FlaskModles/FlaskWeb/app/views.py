# -*- coding:utf-8 -*-

from app import app
from flask import render_template, redirect, session, redirect, url_for, flash
from datetime import datetime
from forms import NameForm
from models import User, Role
from app import db

@app.route('/index', methods=['GET','POST'])
def index():
    # name = None
    form = NameForm()
    if form.validate_on_submit():  # 会便捷的检查该请求是否是一个POST请求以及是否有效
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username= form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''

        # # name = form.name.data
        # # form.name.data = ''  # 将表单中的内容清空
        # # 使用session及重定向
        # old_name = session.get('name')
        # if old_name is not None and old_name != form.name.data:
        #     flash('Look like you have changed your name!')
        # session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template("index.html", form = form, current_time=datetime.utcnow(), name=session.get('name'),
        known = session.get('known', False))

@app.route('/user/<name>')
def user(name):
    if name == 'pitt':
        return render_template('user.html',name = name)
    else:
        return render_template('index.html', name = name)

@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500