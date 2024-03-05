--points table

select team_1,count(team_1) as total_matches,SUM(winflag) as wins,count(team_1)-SUM(winflag) as lose
from( 
select team_1, case when team_1=winner then 1 else 0 end as winflag
from icc_world_cup
union all
select team_2,
case when team_2=winner then 1 else 0 end as winflag
from icc_world_cup)pt
group by team_1
order by wins desc
