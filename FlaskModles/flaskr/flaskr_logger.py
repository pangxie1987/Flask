# -*- coding:utf-8 -*-
'''
邮件和日志记录
'''

import logging
from flask import Flask, render_template
from logging.handlers import SMTPHandler
from threading import Thread


toaddr = ['m18516292278@163.com']
fromaddr = 'm18516292278@163.com'
from_server = ('smtp.163.com', 25)
subject = 'YourApplication Failed!'
credentials = ('m18516292278', 'lpb123456') #(用户名，授权码)

def smtplogger_mail():
    '使用logging模块中的SMTPHandler方法发送邮件'
    errlog = logging.getLogger()
    sh = SMTPHandler(from_server, fromaddr, 
                toaddr, subject,
                credentials=credentials)
    # sh.setLevel(logging.ERROR)

    def mylog():
        errlog.addHandler(sh)

    t1 = Thread(target=mylog)
    t1.start()


# 使用Flask-mail模块发送邮件 https://www.aliyun.com/jiaocheng/465495.html
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 465       #163邮箱使用SSL协议  端口为465
app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'm18516292278@163.com'
app.config['MAIL_PASSWORD'] = 'lpb123456'

mail = Mail(app)

@app.route('/')
def index():
    '访问/ 发送邮件'
    send_mail()
    return 'Email Send Sucess!'

@app.route('/log')
def log():
    '访问/log 写日志'
    
    app.logger.warning('warning message!')
    app.logger.error('Error message!')
    app.logger.info('info message!')
    app.logger.debug('debug message!')
    return 'Log Write Sucess!'
    
def send_async_email(app, msg):
    '异步发送邮件https://blog.csdn.net/leoe_/article/details/70169783'
    with app.app_context():
        mail.send(msg)

def send_mail():
    '创建邮件发送方法'
    msg = Message('hello', sender='m18516292278@163.com', recipients=['m18516292278@163.com'])

    msg.body = 'Flask-Mail Email'
    msg.html = "<b>testing</b>"
    with app.open_resource('flaskr.log') as fp: # 添加附件
        msg.attach('flaskr.log', 'flaskr/log', fp.read() )
    # mail.send(msg)

    thr = Thread(target=send_async_email, args= [app, msg])
    thr.start()
    
if __name__ == '__main__':
    # 创建日志
    handler = logging.FileHandler('flaskr.log', mode='a+')
    handler.setLevel(logging.INFO)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)

    app.run(debug=True)