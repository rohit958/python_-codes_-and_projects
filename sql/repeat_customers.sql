--repeat customers

with fv as(
select customer_id,min(order_date)as first_visit
from customer_orders
group by customer_id
)

select order_date, count(customer_id) as total_customers, SUM(first_visitflag) as new_visits,
 count(customer_id)- SUM(first_visitflag) as repeated_customers from (
select co.*,fv.first_visit, case when order_date=first_visit then 1 else 0 end as first_visitflag from customer_orders co
inner join fv
on co.customer_id=fv.customer_id)cmp
group by order_date
order by order_date
