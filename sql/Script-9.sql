
select *, case 
	when id=(select max(id)from seats) and id%2=1 then id
	when id%2=0 then id-1
	else id+1 end as new_id
	from seats s1
order by id;