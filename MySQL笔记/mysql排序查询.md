#排序查询  #
## 语法 ##
select 查询列表
from表名
(where 条件)
order by 排序列表
**排序列表：**
可以是单个字段、多个字段、表达式、函数、列数以及它们的组合。
升序：asc（默认）
降序：desc



- 例子：
select *
from employees 
where salary>10000
order by salary (asc);
select *
from employees 
where salary>10000
order by salary desc;
- 例子：
 按照姓名的长度降序：
select last_name as ‘姓名’
from employees
order by length(last_name) desc;

## 按照多个字段排序 ##
查询姓名，工资，部门编号，先按照工资升序，再按照部门编号降序
select name,salary,department_id
from employees 
order by salary asc,department_id desc;
## 按照列数排序 ##
select *
from employees
order by 2;
或者select *
from employees
order by first_name;