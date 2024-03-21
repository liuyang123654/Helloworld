#MYSQL启动办法#


1. 在应用中搜索“服务”，然后在里面找到MYSQL，右键启动
2. 

  - 在应用中搜索cmd,右键以管理员身份进入终端.
  - 输入net start mysql

# MYSQL无法启动怎么办 #


1. 在应用中搜索cmd,右键以管理员身份进入终端.
2. 输入mysqld --initialize --user=mysql --console，注意保存一下里面的密码
3. net start mysql（要是报错，就先mysqld --install，在net start mysql)