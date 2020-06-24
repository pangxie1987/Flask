# -*- coding:utf-8 -*-
'''
Flask框架
https://www.v2ex.com/t/376733
https://blog.csdn.net/u011054333/article/details/70151857
'''

from flask import Flask,url_for,request,redirect,render_template

app=Flask(__name__)
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'User %s'%username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d'%post_id

@app.route('/')
def index():
    '''
    index
    '''
    return url_for('/')

@app.route('/login')
def login():
    '''
    login
    '''
    # print(url_for('login'))
    return url_for('login')

@app.route('/user/<username>')
def profile(username):
    '''
    profile
    url_for()根据函数名称和参数返回地址
    '''
    # print(url_for('profile',username='zhangsan'))
    return url_for('profile', username=username)

@app.errorhandler(404)
def not_found():
    '''
    def not_found
    '''
    return 'not found',404

@app.route('/about')
def about():
    '''
    def about
    '''
    return not_found()

@app.route('/logout/',methods=['GET','POST'])
def logout():
    '''
    logout
    redirect()重定向，value1=重定向后的位置，value2=重定向方式301：永久重定向，302：暂时重定向
    '''
    name  = request.args.get('name')
    if not name:
        return redirect(url_for('login'),code=302)
    else:
        return name

'''
静态文件，使用url_for()
url_for('static',filename='style.css')
'''

@app.route('/hi/')
@app.route('/hi/<name>')
def hi(name=None):
    '''
    调用模板，模板为templates目录hi.html
    '''
    return render_template('hi.html',name=name)


# with app.test_request_context():
#     print url_for('index')
#     print url_for('login')
#     print url_for('login',next='/')
#     print url_for('profile',username='Jone Doe')

if __name__=='__main__':
    # host='0.0.0.0'  在docker中运行需要将host设置为'0.0.0.0'
    app.run(debug=True,host='0.0.0.0')