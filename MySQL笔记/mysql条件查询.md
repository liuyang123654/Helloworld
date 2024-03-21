# 条件查询 #
select 查询内容
from 表名
where 筛选条件；
**顺序：from，where,select**
例如：select last_name,first_name from where salary >20000;
- 筛选条件：关系表达式/逻辑表达式：
## 关系表达式 ##
> < >= <= = <>(不等于)
## 逻辑表达式 ##
Java：&& || !
sql:and or not 
例子：select last_name,department_id
from employees where department_id<50 or department_id>100;(或where not department>=50 and department_id<=100;)
