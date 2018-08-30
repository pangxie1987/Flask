# -*- coding:utf-8 -*-
'''
使用selenium运行测试的框架
'''
import time
import unittest
import threading
from selenium import webdriver
from app import db, create_app, fake
from app.models import User, Role, Post

class SeleniumTestCase(unittest.TestCase):
    client = None
    @classmethod
    def setUpClass(cls):
        # 启动浏览器
        options = webdriver.ChromeOption()
        options.add_argument('headless')
        try:
            cls.client = webdriver.Chrome(chrome_options=options)
        except:
            pass
        # 如果无法启动浏览器  则跳过这些测试
        if cls.client:
            cls.app = create_app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()

            # 禁止日志，保持输出简洁
            import logging
            logger = logging.getLogger('werkzeug')
            logger.setLevel('ERROR')

            # 创建数据库， 使用一些虚拟数据填充
            db.create_all()
            Role.insert_roles()
            # User.generate_fake(10)
            # Post.generate_fake(10)
            fake.users(10)
            fake.posts(10)


            #添加管理员
            admin_role = Role.query.filter_by(permissions=0xff).first()
            admin = User(email='john@example.com',
                        username = 'john', password='cat',
                        role = admin_role, confirmed=True)
            db.session.add(admin)
            db.session.commit()

            # 在一个线程中启动Flask服务器
            cls.server_thread = threading.Thread(target=cls.app.run, kwargs={'debug':False})
            cls.server_thread.start()
            time.sleep(1)

        @classmethod
        def tearDownClass(cls):
            if cls.client:
                # 关闭Flask服务器和浏览器
                cls.client.get('http://localhost:5000/shutdown')
                cls.client.close()

                # 销毁数据库
                db.drop_all()
                db.session.remove()

                # 删除程序上下文
                cls.app_context.pop()

        def setUp(self):
            if not self.client:
                self.skipTest('Web browser not avalable')

        def tearDown(self):
            pass
