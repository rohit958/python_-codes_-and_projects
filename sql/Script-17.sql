with CTE AS(
	select manager_name, count(*) over(partition by manager_name) as employee_count,
	count(* ) over(partition by department) as dept_count,
	department  from(
		select e.*
			,m.name as manager_name 
				from employee e join employee m
				on m.id=e.managerid
))

select distinct manager_name, department, employee_count from CTE where dept_count>=10 and employee_count>=5;
				