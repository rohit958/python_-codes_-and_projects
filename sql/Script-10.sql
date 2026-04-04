-- last 7 successful runs  ,total runs, last succeful run_id
WITH last_7 AS (
    SELECT 
        data_set_id,
        run_id,
        ended_at,
        CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END AS status_flag
    FROM pipeline_run
    WHERE started_at >= CURRENT_TIMESTAMP - INTERVAL '7' DAY
),

ranked_success AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY data_set_id 
               ORDER BY ended_at DESC
           ) AS rn
    FROM last_7
    WHERE status_flag = 1
),

sr AS (
    SELECT 
        l.data_set_id,
        COUNT(l.run_id) AS total_runs,
        SUM(l.status_flag) AS successful_runs
    FROM last_7 l
    GROUP BY l.data_set_id
)

SELECT 
    sr.data_set_id,
    rs.ended_at AS last_successful_run,
    rs.run_id AS last_successful_run_id,
    sr.total_runs,
    sr.successful_runs * 1.0 / sr.total_runs AS success_rate
FROM sr
LEFT JOIN ranked_success rs
    ON sr.data_set_id = rs.data_set_id
    AND rs.rn = 1;