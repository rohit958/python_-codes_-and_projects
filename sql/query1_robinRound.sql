with t2 as (
select *, row_number () over(order by team) as id from match) 

select *
from t2 a
join t2 b on a.team <>b.team
where a.id<b.id
