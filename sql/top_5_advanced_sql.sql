--query to get date of 5 months back
--select current_date - Interval'5 months';

--Q1: management wants data of users didn't logged from past 5 months

-- get the login data for past 5 months.
-- find active users with user id.
-- return username 

/*
select user_id,max(login_timestamp) from logins
group by user_id
having  max(login_timestamp) < current_date - Interval'5 months';
*/

--Q2 get the count of users and session per quarter
/*
select extract( QUARTER from login_timestamp) as quarter, count(*) as sessions,
count(distinct user_id) as user_counts, min(login_timestamp) as first_login
from logins
group by extract( QUARTER from login_timestamp);
*/
 
--Q3 display user which login in January 2024 but not in November2023
/*
select distinct user_id from logins where login_timestamp between '2024-01-01' and '2024-01-31' EXCEPT
select user_id from logins where login_timestamp between '2023-11-01' and '2023-11-30'; -- Minus in other sql languages
*/

--Q4 percentage change in sessions from quarters

with cte as(
select extract (Quarter from login_timestamp) as quarter,count(*) as sessions,
count(distinct user_id) as user_counts, min(login_timestamp) as first_login
from logins
group by extract (Quarter from login_timestamp) 
	order by first_login
	)

select *,
lag(sessions,1) over(order by first_login) as prev_ss,
sessions- lag(sesssion)
	
