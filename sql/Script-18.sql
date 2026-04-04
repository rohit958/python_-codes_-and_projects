
with CTE as(
select t.revenue, extract(month from t.transaction_date) as month,s.* from transactions t join sectors s
on t.company_id=s.company_id)

select month, sector, avg(revenue) as avg_revenue from CTE 
group by month, sector
order by month

