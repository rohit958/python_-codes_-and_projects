select * from employee


--masking last two digits of salary
select empname, concat(left(cast(salary as text),(length(cast(salary as text)))-2),'XX') from employee

-- even odd employees
--even
select * from (
select *,row_number() over(order by empid) as rowNum from employee) as emp
where emp.rowNum%2=0

--odd
select * from (
select *,row_number() over(order by empid) as rowNum from employee) as emp
where emp.rowNum%2<>0

--male percent in company
select count(*) filter(where gender ='M')*100/count(*) as malepct from employee 

-- employee name starts with 'A'

select * from employee where empname like'A%'

-- employee name with 2nd letter 'a'

select * from employee where empname like'_a%'

-- employee name with 2nd last letter 'y'

select * from employee where empname like'%y_'

--starting with vowels
select * from employee where lower(empname) similar to '[aeiou]%'

--ending with vowels
select * from employee where lower(empname) similar to '%[aeiou]'

--2nd highest salary
select * from employee order by salary desc
limit 1 offset 1


--2nd highest salary
select * from employee e1
where 2=
(
select count(distinct e2.salary) from employee e2
where e2.salary>=e1.salary)

--query to find duplicate

select count(*),empid from employee
group by empid
having count(*)>1;

--query to delete duplicate records
delete from employee where empid in
(select empid from employee
 group by empid 
 having count(*)>1)




-- query to find people working in same project
with CTE as(
select emp.empname,emp.empid,emp.city, d.project,d.empposition
from employee emp 
join employeedetail d
on emp.empid=d.empid)

select a.empname,a.empid,a.city, a.project
from CTE a, CTE b
where a.project=b.project and a.empid<>b.empid


--people with highest salary in each project
with CTE as(
select emp.empname,emp.empid,emp.salary, d.project, row_number() over(partition by d.project order by emp.salary desc)
from employee emp 
join employeedetail d
on emp.empid=d.empid
)

select empname,empid,salary as max_salary, project from CTE
where row_number =1


--simple join but with limited data to get max_salary in each project
select d.project,max(emp.salary)as maxsal
from employee emp 
join employeedetail d
on emp.empid=d.empid
group by d.project
order by maxsal desc

