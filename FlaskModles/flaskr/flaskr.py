# -*- coding:utf-8 -*-
'''
flaskr主程序
'''
from __future__ import with_statement
import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash, url_for
from contextlib import closing


# configuration
DATABASE = "tmp\\flaskr.db"
DEBUG = True
SECRET_KEY = 'development.py'
USERNAME = 'pitt'
PASSWORD = 'pitt'

# crete our little application
app = Flask(__name__)
app.config.from_object(__name__)

# import flaskr_logger

def connect_db():
    '初始化数据库连接'
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    '导入schema.sql数据库初始化脚本'
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
    print('sqlite3 insert sucess!')

@app.before_request
def before_request():
    '在请求之前调用， 没有参数'
    g.db = connect_db()

@app.teardown_request
def teardown_request(Exception):
    '在响应构造后执行'
    g.db.close()

@app.route('/')
def show_entries():
    '''
    查询数据库中的所有条目，并按照id倒叙
    '''
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    '处理用户插入新的文本'
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values(?, ?)',[request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was sucessfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    '用户登录请求处理'
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were Logged In')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    '处理用户的登出请求'
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    
    # import logging
    # from logging.handlers import SMTPHandler
    # ADMINS = ['m18516292278@163.com']
    # sender = 'm18516292278@163.com'
    # import logging
    # logger = logging.getLogger()
    # # ('smtp.163.com', 25)
    # mail_handler = SMTPHandler(('smtp.163.com', 25), sender, 
    #             ADMINS, 'YourApplication Failed!',
    #             credentials=('m18516292278', 'lpb123456'))
    # mail_handler.setLevel(logging.ERROR)
    # #if not app.debug:
    # logger.addHandler(mail_handler)
    # print('Mail Error')
    app.run('0.0.0.0')
