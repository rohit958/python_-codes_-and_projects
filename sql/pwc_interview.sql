--PWC interview question - company whose growth is positive in 3 years continuosly

with CTE as(
select *,lag(revenue) over(partition by company) as prev_rev,
(revenue-lag(revenue) over(partition by company)) as diff,
count(company) over(partition by company) as yearcnt
from company_revenue
)
/*
select company,yearcnt, count(1) as cnt from CTE 
where diff>0
group by company, yearcnt
having yearcnt=3 and count(1) =2
*/
select distinct company from CTE where company not in (select company from CTE where diff<0)




