# 基础查询 #
例：select stuid from stuinfo;
(执行顺序：1.from；2.select语句)
## 查询常量 ##
select 100;
## 查询表达式 ##
select 100/3;
## 查询单个字段 ##
select `last_name` from stuinfo;(那个符号是着重号，用来表示一个整体)
## 查询多个字段##
select 'last_name','email','stuid' from stuinfo;(注意中间是逗号)
##查询所有字段##
select * from stuinfo;
但是要是想让数据按一定顺序出来，还是可以按照前面查询多个字段的方法。(注意格式规范：即查询的每一个字段占一行)**快捷键：选中这个语句按 f12**
## 查询函数 调用获取返回值） ##
select database();
select version();
select user();
## 起别名 ##
1. as关键字
例：select user() as ‘用户名’；（这个用户名加不加引号均可，最好是加）
select 'first_name' as 'name' fro stuinfo;

2. 使用空格(把as换成空格)
## 按照需求 拼接##
concat拼接函数
例：select concat(first_name,lase_name) as 'name' from stuinfo;
## 去掉重复项 ##
distinct关键字
例:select distinct department_id from employees;
## 查看表的结构 ##
desc 表名；
show columns from 表名；
## ifnull ##
select ifnull(表达式1，表达式2） from 表名
功能：如果表达式1为null,显示表达式2，否则显示表达式1



**千万注意MYSQL中+只做加法运算**
- 其中一个数是字符，就将其转换成数值型，在运算。转换不了的直接变成0
- null+任何都是null
