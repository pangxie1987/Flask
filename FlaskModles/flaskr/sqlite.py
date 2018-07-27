# -*- coding:utf-8 -*-
'''
用于将初始化数据插入数据库
'''
import sqlite3, os

conn = sqlite3.connect("tmp\\flaskr.db")
cur = conn.cursor()

cur.execute("drop table if exists entries;")
cur.execute('''create table entries(
    id integer primary key autoincrement,
    title string not null,
    text string not null);''')

