# -*- coding:utf-8 -*-
'''
create tables use db
insert datas to tables
add data
commit
'''
import os
from app import db
from app.models import User, Role
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from migrate.versioning import api

def create_db():
    '''
    创建数据库表，并添加数据
    '''
    db.drop_all()   #删除所有表
    db.create_all() # 创建表

    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_john = User(username='john', role=admin_role)
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)

    db.session.add_all([admin_role, mod_role, user_role,user_john, user_susan, user_david])
    db.session.commit()

    print('users and roles create sucess !')
    print(admin_role.name)


if __name__ == '__main__':

    create_db()
    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

    #--------------查询--------------
    users_all = User.query.all()    #查询所有users表中的数据
    users_id = User.query.filter_by(id=1).all() #根据users中的id过滤筛选
    user_role = Role.query.filter_by(name='User').first()
    print(users_all)
    print(users_id)
    print(user_role)