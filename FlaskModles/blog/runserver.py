# -*- coding:utf-8 -*-
'''
blog主函数目录，运行此文件
'''
from blog import app

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)