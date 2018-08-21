# -*- coding:utf-8 -*-
'''
flask 发送邮件
https://blog.csdn.net/wbin233/article/details/73222027
'''
from . import mail
from flask_mail import Message
from threading import Thread
from flask import current_app
# from flask import Flask
# from flask import request
# from flask_script import Manager, Shell
# from flask_mail import Mail, Message
# from threading import Thread

# app = Flask(__name__)
# app.config['MAIL_DEBUG'] = True             # 开启debug，便于调试看信息
# app.config['MAIL_SUPPRESS_SEND'] = False    # 发送邮件，为True则不发送
# app.config['MAIL_SERVER'] = 'smtp.163.com'   # 邮箱服务器
# app.config['MAIL_PORT'] = 25               # 端口
# # app.config['MAIL_USE_SSL'] = True           # 163邮箱不需要
# # app.config['MAIL_USE_TLS'] = False          # 不需要使用TLS
# app.config['MAIL_USERNAME'] = 'm18516292278@163.com'  # 填邮箱
# app.config['MAIL_PASSWORD'] = 'lpb123456'      # 填授权码
# app.config['MAIL_DEFAULT_SENDER'] = 'm18516292278@163.com'  # 填邮箱，默认发送者
# manager = Manager(app)
# mail = Mail(app)


# # 异步发送邮件
# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)

# @app.route('/')
# def index():
#     msg = Message(subject='Hello World',
#                   sender="m18516292278@163.com",  # 需要使用默认发送者则不用填
#                   recipients=['m18516292278@163.com', 'm18516292278@163.com'])
#     # 邮件内容会以文本和html两种格式呈现，而你能看到哪种格式取决于你的邮件客户端。
#     msg.body = 'sended by flask-email'
#     msg.html = '<b>测试Flask发送邮件<b>'
#     with app.open_resource('run.py') as fp: # 添加附件
#         msg.attach('run.py', 'run/py', fp.read() )
#     thread = Thread(target=send_async_email, args=[app, msg])
#     thread.start()
#     # mail.send(msg)
#     return '<h1>邮件发送成功</h1>'

def send_async_email(app, msg):
    '''
    邮件发送需要在程序的上下文中进行，
    新的线程中没有上下文，需要手动建立
    '''
    with app.app_context():
        mail.send(msg)

def s_Mail(subject, recipients, attachfile):
    '''
    封装函数发送邮件，使用多线程方式
    '''
    app = current_app._get_current_object()
    msg = Message(subject=subject,
                  recipients=recipients)
    msg.body = 'sended by flask-email'
    msg.html = '<b>测试Flask发送邮件<b>'
    with app.open_resource(attachfile) as fp:
        msg.attach(attachfile, 'run/py', fp.read())
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    print('Email Send Sucess!')
    

# if __name__ == '__main__':
#     s_Mail()