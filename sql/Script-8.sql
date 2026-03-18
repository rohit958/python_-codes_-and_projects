
--most ordered dish in each month

with most_ordered_dish as(
--most ordered dish in each month
select distinct dish_name, order_month from(

select dish_name, order_month, rank() over(partition by order_month order by order_count desc) from
(
select dish_name,(extract(year from order_date)||'-'||extract (month from order_date)) as order_month,
count(*) as order_count
from orders_food 
group by dish_name, (extract(year from order_date)||'-'||extract (month from order_date))
)
)
where rank=1
order by order_month),




 active_user as(--active user
-- considered acrtive if user orders atleast once in a month
select (extract(year from order_date)||'-'||extract (month from order_date)) as order_month,
count(distinct user_id) as active_user_count
from orders_food 
group by (extract(year from order_date)||'-'||extract (month from order_date))

)

select m.order_month,m.dish_name as most_ordered_dish , a.active_user_count from active_user a join most_ordered_dish m
on a.order_month=m.order_month