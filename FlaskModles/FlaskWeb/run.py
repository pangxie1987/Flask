# -*- coding:utf-8 -*-
'''
<Flask Web开发>
run this file
'''
from app import app
from db_create import create_db

# @app.route('/abc')
# def index():
#     return render_template('index.html')


if __name__ == '__main__':
    create_db()
    app.run(debug=True)