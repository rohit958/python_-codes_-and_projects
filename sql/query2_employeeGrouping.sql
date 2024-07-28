--select * from emp
--Ntile() groups data upto the value which has been passed
-- String_agg()- clubs rows data into single rows

with t1 as(
select CONCAT(id,' ',name) as text, NTILE(4) over(order by name asc) as Groups from emp
)

select STRING_AGG(t1.text,', '), t1.Groups from t1
group by t1.Groups
order by t1.Groups asc 