# -*- coding:utf-8 -*-
'''
flaskr的单元测试框架
'''
import os
import flaskr
import unittest
import tempfile

class FalskrTestCase(unittest.TestCase):
    
    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def login(self, username, password):
        '向登录发出post请求，并携带表单数据'
        return self.app.post('/login', data=dict(
            username=username, password=password), follow_redirects=True)

    def logout(self):
        '登出请求get'
        return self.app.get('logout', follow_redirects=True)

    def test_empty_db(self):
        '测试案例：检查访问根路径时，正确返回了 No entries here so far'
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

    def test_login_logout(self):
        '测试登录和登出'
        rv = self.login('pitt', 'pitt')
        assert 'You were Logged In' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('pitty', 'pitt')
        assert 'Invalid username' in rv.data
        rv = self.login('pitt', 'pitty')
        assert 'Invalid password' in rv.data

    def test_message(self):
        '测试消息的添加是否正常'
        self.login('pitt', 'pitt')
        rv = self.app.post('/add', data=dict(
        title='<Hello>', text='<strong>HTML</strong> allowed here'), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert '&lt;Hello&gt;' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data

if __name__ == '__main__':
    unittest.main()
