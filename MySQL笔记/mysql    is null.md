# is null #


- 例：查询没有奖金的员工信息
select *
from employees
where commission_pct is null;
- 例：查询有奖金的员工信息
select *
from employees
where commission_pct is not null;
**注：这里的null不能用=代替**
**区别： =判断普通内容；is 只能判断NULL值 <=> (安全等于)，二者都能判断**
