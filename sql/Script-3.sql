
with t1 as(
select empd_id, swipe as swipe_outtime, row_number() over () as rn from clocked_hours
where flag='O')

,t2 as (
select empd_id, swipe as swipe_intime, row_number() over () as rn from clocked_hours
where flag='I')


select t1.empd_id,sum(abs(extract(hour from (t1.swipe_outtime-t2.swipe_intime)))) as total_hours from t1 join t2 on t1.rn=t2.rn
group by t1.empd_id