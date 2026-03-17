


select *,(cases*100 /cum_sum) as pct_incr from (
select *, sum(cases) over(order by month
rows between unbounded preceding and 1 preceding) as cum_sum from 
(
select extract(month from record_date) as month, sum(cases_count) as cases from covid_cases 
group by (extract(month from record_date))
)
)
