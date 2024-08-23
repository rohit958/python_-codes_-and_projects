--Solution 1:
with temp as(
select state, city,population,max(population) over(partition by state) as maxp,min(population) over(partition by state)as minp from city_population
)

select * from (
select state, 
	max(case when population=maxp  then city end) as max_population, 
	max(case when population = minp then city end) as min_population from temp
	group by state
) 


--Solution 2:


with temp as(
select state, city,population,row_number() over(partition by state order by population)as rn,
	row_number() over(partition by state order by population desc)as rn2 from city_population
)

select a.state,a.city as min_population_city,b.city as max_population_city
from temp a join temp b
on a.state=b.state
where a.rn=1 and b.rn2=1