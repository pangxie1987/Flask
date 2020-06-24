from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'nickname':'Miguel'}
#     posts = [
#         {
#             'author':{'nickname':'John'},
#             'body':'Beautiful day in ShangHai!'
#         },
#         {
#             'author':{'nickname':'Pitt'},
#             'body':'Beautiful day in BeiJing!'
#         },
#         {
#             'author':{'nickname':'MaGa'},
#             'body':'Beautiful day in ChongQing!'
#         }
#     ]
#     return render_template('index.html',
#     title = 'Home',
#     user = user,
#     posts =posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for OpenId="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')

    return render_template('login.html', 
    title = 'Sign In',
    form = form,
    providers = app.config['OPENID_PROVIDERS'])