#in关键字#


1. 查询部门编号是30/50/90的员工名字和部门编号


 - select last_name,department_id
from employees
where department_id in      (30,50,90);
 - select last_name,department_id
from employees
where department_id =30
or  department_id =50
or department_id =90;
1. 查询工种编号不是SH_CLERK或IT_PROG的员工信息
 
 -select *
from employees
where jod_id not in ("SH_CLERK","IK_PROG"); 
# (not) between and      
select department_id
from employees
where id between 30 and 90;

