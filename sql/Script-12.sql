-- top 5 coins and token with largest value


with CTE as(
select coin_name as coin_or_token, 
(quantity * (cast(regexp_replace(unit_value,'[$,]', '', 'g') as decimal))) as total_value ,'coin' as type
from coins 

union
select token_name as coin_or_token, 
(quantity * (cast(regexp_replace(unit_value,'[$,]', '', 'g') as decimal))) as total_value , 'token' as type
from tokens )


select * from (
select *, dense_rank() over( partition by type order by total_value desc) as rnk from CTE)
where rnk<=5


