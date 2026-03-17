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