select customer_id, sum(total_amount) from orders
where  order_date >= NOW() - INTERVAL '1 year'
group by customer_id order by 2 desc
limit 3;



select current_timestamp - interval '1 month'