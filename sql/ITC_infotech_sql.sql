--ITC infotech sql question



--self join
--select *,row_number() over() as rn from city_distance
--order by distance;


select * from(
select *,row_number() over(partition by distance)as rn from city_distance
order by distance)
where rn=1;

