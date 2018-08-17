import os, sys
from flask import Flask, current_app
from flask_script import Manager

# print('1:',os.path.dirname(__file__))
# print('2:',os.path.dirname(os.path.abspath(__file__)))
# print('3:',os.path.abspath(sys.argv[0]))

app = Flask(__name__)
# app_ctx = app.app_context()
# app_ctx.push()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()