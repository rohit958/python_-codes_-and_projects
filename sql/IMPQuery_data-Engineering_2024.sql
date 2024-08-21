1. How would you handle duplicate records in a SQL table?
Ans: select distict id from customers;
	select *, row_number() over(partitioned by ID ) as rn from customers
	where rn=1;

2. Write a SQL query to find the second highest salary from an employee table.
	select *, dense_rank() over(id order by id desc) from employee
	where rn=2;

3. How would you optimize a slow-running query in a large dataset?
	
	Indexing on the table.
	partitioned on indexes.
	using CTEs to avoid re-exicuting of sub-queries.
	Explain and analyse
	query catching
	Creating Materialized Views
	Normalization and Denormalization
	

4. Explain how you would perform a self-join and in what scenarios it is useful.
	self join can be used on joining columns of the same table.
	it is usefull when we need to comapare the records of the same table.
	


5. Write a SQL query to get the cumulative sum of a column in a table.
	select *, sum(salary) over( rows between unbounded preceding and current row) as running_sum from employee
	order by id;


6. How would you implement pagination in SQL?
	limit-used to limit the result to defined number of rows
	offset- starting point
	



7. Write a query to find all employees who have the same salary.
	
	select distinct a.id,a.name,a.salary from employees_allah a
	join employees_allah b on a.salary=b.salary
	where a.id!=b.id
	order by salary



8. Explain how you would delete duplicate rows from a table, keeping only one instance.

	 with cte(
	 select id, row_number() over(partition by id) as rn from employee)
	
	delete from employee where id in (select id from cte where rn>1);


9. How would you find the most common value in a column?
	
	--most common salary
	select mode() within group(order by salary) from employees_allah
	
	--group by count



10. Write a SQL query to retrieve all rows where the date is within the last 30 days.
	
	select * from patients_table where transanction_id >(select current_date - Interval'1 months') 