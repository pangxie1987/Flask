Flask框架测试
runserver.py为运行文件
参考 
https://www.cnblogs.com/mysql-dba/p/6070258.html

mysql安装
version：mysql-5.7.17-win32.zip
1、解压
2、目录下添加my.ini配置文件，注意basedir  datadir 用 C:/WorkDay/mysql-5.7.17 这种形式
3、安装 用户管理员cmd  cd mysql\bin   mysqld --initialize     mysqld install
4、启动服务  net start mysql
5、原始密码登录 mysql -u root -p  (原始密码在mysql\data\XXX.err文件中)
6、重置密码ALTER USER 'root'@'localhost' IDENTIFIED BY 'newpassword';
7、本次测试mysql  C:\WorkDay\mysql-5.7.17  root/123456