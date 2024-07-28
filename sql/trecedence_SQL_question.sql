--output consecutive seats in cinema atleast two consecutive seats


/*-- approach 1 cte
--Query complete 00:00:00.065
with cte as(
select seat_id,free,row_number() over() as rn, (seat_id - row_number() over()) as grp
 from cinema
where free=1)

select seat_id from(
select seat_id, count(*) over(partition by grp) as grp_cnt from cte)
where grp_cnt>1



-- aproach 2 self join Query complete 00:00:00.056
with cte as (
select c1.seat_id as s1,c2.seat_id as s2 from cinema c1
left join cinema c2 on c1.seat_id=c2.seat_id+1
where c1.free=1 and c2.free=1)

select s1 from cte
union
select s2 from cte

*/



