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



