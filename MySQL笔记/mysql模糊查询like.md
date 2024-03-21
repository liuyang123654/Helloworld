# 模糊查询 #
## like ##


- 例：查询姓名中带a的字符的员工信息
select * 
from employees
where last_name like '%a%';
- 例：查询姓名中第一个字符为a的的员工信息
select * 
from employees
where last_name like 'a%';
- 例：查询姓名中第三个字符为a的的员工信息
select * 
from employees
where last_name like '__a%';（前面两个下划线）
- 例：查询姓名中最后一个字符为a的的员工信息
select * 
from employees
where last_name like '%a';- 例：查询姓名中第三个字符为-的的员工信息
select * 
from employees
where last_name like '__￥_%' escape '$';（说明$为转义字符）

