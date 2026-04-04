-- Step 1: Create the table
CREATE TABLE job_runs (
    job_status VARCHAR(10) CHECK (job_status IN ('success', 'fail')),
    run_date DATE NOT NULL
);

-- Step 2: Insert sample data
INSERT INTO job_runs (job_status, run_date)
VALUES
    ('success', '2025-08-01'),
    ('success',  '2025-08-02'),
    ('fail', '2025-08-03'),
    ('fail',    '2025-08-04'),
    ('success', '2025-08-13');




select job_status,start_date, end_date from(

	select job_status, min(run_date) as start_date,max(run_date) as end_date,grp 
	from 
		(
		SELECT *,
		       run_date - (ROW_NUMBER() OVER (PARTITION BY job_status ORDER BY run_date)) * INTERVAL '1 day' AS grp
		FROM job_runs
		)
group by job_status , grp
order by job_status,grp )