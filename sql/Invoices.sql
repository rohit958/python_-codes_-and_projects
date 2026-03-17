--select * from invoices 

-- top 3 spenders of UPI
select customer_name,sum(total_amount) as total_spending from invoices
where payment_method='UPI'
group by customer_name
order by 2 desc 
limit 3;

-- total smartphone purchased in july months
select sum(quantity) from invoices 
where item_name ='Smartphone' and extract(month from invoice_date)=07;

-- 

select * from invoices;


--top 3 purchasing of customers 
with purchases as(
select customer_name,total_amount ,dense_rank() over( partition by customer_name order by total_amount desc) as highest_purchase from invoices)

select customer_name, total_amount, highest_purchase from purchases
where highest_purchase<3;
;

--running total of each customer

select *, sum(total_amount) over( partition by customer_name order by invoice_date) from invoices;


--lead and lag 
select *, lead(total_amount,1,0) over(partition by customer_name order by invoice_date) from invoices ;

select *, lag(total_amount,1,0) over(partition by customer_name order by invoice_date) from invoices ;


--three months moving average
with monthly_sum as(
select extract(month from invoice_date) as month, sum(total_amount) as monthly_total from invoices
group by 1)

select month, round(avg(monthly_total) over(rows between 1 preceding and 1 following),2) as three_month_mov_avg
from monthly_sum
order by 1;



