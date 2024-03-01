-- delloite interview question
--calculate total in time of each employee


with intime as(
select empd_id,swipe as intime,row_number() over(partition by empd_id) from clocked_hours 
where flag='I'
),

outtime as(
select empd_id,swipe as outtime,row_number() over(partition by empd_id) from clocked_hours 
where flag='O'
)
select outtime.empd_id, sum(outtime.outtime - intime.intime)  as duration
from intime, outtime
where intime.empd_id=outtime.empd_id
and intime.row_number=outtime.row_number
group by 1


--employee status

select coalesce(e2.emp_id,e21.emp_id),
case when e2.emp_id=e21.emp_id and e2.designation!=e21.designation then 'promoted'
	when e2.emp_id is NULL then 'new_joinee'
	when e21.emp_id is NULL then 'resignned'
	else 'same_postion' end as designation_status
from emp_2020 e2 FULL OUTER JOIN
emp_2021 e21 on e2.emp_id=e21.emp_id
where coalesce(e2.designation,'xxx')!=coalesce(e21.designation,'yyy')

