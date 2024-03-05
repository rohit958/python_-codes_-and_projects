--flight soruce and destination
with flight as( 
select *,count(*) over(partition by cid) totalflights, row_number() over(partition by cid)as flightNumber from flights 
)

select cid,MAX(origin) as origin,max(destination) as destination from(
select cid, case when flightNumber=1 then origin end as origin,
case when flightNumber=totalflights then destination end as destination
from flight)
group by cid

--new customer count in each month
select order_date,count(distinct customer) as new_customers from(
select order_date,customer,row_number() over(partition by customer order by order_date)as rn from sales
)where rn=1
group by order_date
