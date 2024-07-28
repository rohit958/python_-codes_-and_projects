-- recommend the pages likes by friends of users

with cte as(
select  distinct f.user_id,l.page_id,f.friend_id from friends f
inner join likes l on f.friend_id= l.user_id
	order by f.user_id
)

select user_id, page_id from cte 
where (user_id,page_id) not in(select user_id,page_id from likes )

--select * from likes

--select * from friends