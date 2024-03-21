

----------
# MYSQL #
## 登录： ##
1. win+r
2. 输入cmd
3. 输入：mysql -uroot -p
4. 输入密码
**最好用这种方法**
##退出##
exit 或者 ctrl+c
## 注意事项 ##


1. 库名、表名、字段名建议大写；其他关键字建议小写。（不过这个不会有太大问题）
2. 注释：单行：#或者--    ；  多行/*   */。
3. 一条长命令可以换行写
## 一些基本命令 ##
1. 查看版本 select version();**一定记得加括号；**  如果是在cmd中，mysql --version;
1. show databases **一定注意结尾加分号或者是\g**。
2. use ****是打开一个库；
   之后show tables;  //或者是show tables from ****;（table在这里是表的意思）。
3. 查看自己所在的库 select database();**一定记得加括号**。
4. 修改所在库时，直接use+想要进的库名。 
4. 建表**千万注意一定要在进入那个库之后才能进行建表操作**：create table 表名（
        id int，
        name varchar(20) );   **如果显示Query OK 代表成功了**
5. 建表成功之后，输入命令show tables;就可以显示出你所在的库中有哪些表
6. 展示表： desc 表名；(即：显现表中有哪几项）；
想给表加或减项：
alter table **（注意这里table别丢）**stuinfo add column email vachar(20);(增加一项email)
7. 想看表中有哪些数据  select * from 表名；
8. 向表中插入数据： insert into 表名 （id,name）(前面的这个括号也可以不写)values (1,"lucy");  这时候再用7中的select * from 表名，就可以看到你插入的数据了。
9. 修改表中数据： 例如：update stu set name="lily" where id=1;
10. 删除表中数据： 例如：delete from stu where id=1;
11. 删除整个表格：drop table stuinfo;
11. 如果字符格式不正确，要修改的话：(报错：incorrect string value),语句是set names gbk;(修改字符集为gbk)