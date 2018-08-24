# -*- coding:utf-8 -*-
'''
视图文件
'''

from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app, abort, current_app, flash
from . import main
from .forms import NameForm, EditProfileForm
from .. import db
from ..models import User
from ..send_mail import s_Mail
from ..logger import WrLog
from flask_login import login_required, current_user

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

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user = user)

@main.route('/')
def home():
    return redirect(url_for('.index'))

# @main.errorhandler(404)
# def page_not_fount(e):
#     return render_template('404.html'), 404

# @main.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500

@main.route('/edit-profile', methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)