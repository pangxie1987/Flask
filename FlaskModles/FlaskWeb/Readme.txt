《Flask Web开发——基于Python的Web应用开发实践》
https://github.com/miguelgrinberg/flasky
1、创建数据库及迁移脚本 python db_move.py db init
2、更新数据库  python manage.py db upgrade
3、回退数据库  python manage.py db downgrade

4、启动服务 python manage.py runserver

python manage.py db migrate

查看可执行的命令
./FalskWeb
python manage.py

问题
1、reset password报错




创建数据库升级脚本
python manage.py db init
升级
python manage.py db upgrade
降级
python manage.py db downgrade

创建表
python manage.py shell
from app import db
db.create_all()