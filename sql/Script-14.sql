
CREATE TABLE monthly_sales (product_id INT, year_month DATE, qty INT);
INSERT INTO monthly_sales VALUES
 (1,'2025-06-01',100),(1,'2025-07-01',90),(1,'2025-08-01',80), -- declining
 (2,'2025-06-01',50),(2,'2025-07-01',60),(2,'2025-08-01',55);

--input 

select * from
	(

	select product_id,year_month as year_start_month,
	qty as qty1,
	lead(qty) over(partition by product_id order by year_month,qty desc)as qty2,
	lead(qty,2) over(partition by product_id order by year_month,qty desc)as qty3 from monthly_sales
	)
where qty1> qty2 and qty2>qty3 ;

