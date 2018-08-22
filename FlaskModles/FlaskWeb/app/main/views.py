# -*- coding:utf-8 -*-
'''
视图文件
'''

from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from ..send_mail import s_Mail
from ..logger import WrLog
from flask_login import login_required

wlog = WrLog()
@main.route('/index', methods=['GET','POST'])
def index():
    # name = None
    form = NameForm()
    
    if form.validate_on_submit():  # 会便捷的检查该请求是否是一个POST请求以及是否有效
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username= form.name.data)
            db.session.add(user)
            session['known'] = False
            # s_Mail('new user %s is coming' % user, current_app.config['RECEVIERS'], 'send_mail.py')
            wlog.wlog_warning('new user %s is coding' % form.name.data)
        else:
            session['known'] = True
            
            # s_Mail('old user %s is coming' % user, current_app.config['RECEVIERS'], 'send_mail.py')
            wlog.wlog_error('old user %s is coding' % form.name.data)
        session['name'] = form.name.data
        form.name.data = ''

        # # name = form.name.data
        # # form.name.data = ''  # 将表单中的内容清空
        # # 使用session及重定向
        # old_name = session.get('name')
        # if old_name is not None and old_name != form.name.data:
        #     flash('Look like you have changed your name!')
        # session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template("index.html", form = form, current_time=datetime.utcnow(), name=session.get('name'),
        known = session.get('known', False))

@main.route('/user/<name>')
def user(name):
    if name == 'pitt':
        return render_template('user.html',name = name)
    else:
        return render_template('index.html', name = name)

@main.route('/')
def home():
    return redirect(url_for('.index'))

# @main.errorhandler(404)
# def page_not_fount(e):
#     return render_template('404.html'), 404

# @main.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500

# # 保护路由
# @app.route('/secret')
# @login_required
# def secret():
#     return 'Only authenticated users are allowed!'