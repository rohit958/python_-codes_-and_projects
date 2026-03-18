
--calculate max streak

/*
 * solution :- 
 * event_date- row_number() to create group*/

SELECT 
    user_id,
    MAX(streak_length) AS max_streak
FROM (
    SELECT 
        user_id,
        COUNT(*) AS streak_length
    FROM (
        SELECT 
            user_id,
            event_date,
            event_date - 
            ROW_NUMBER() OVER (
                PARTITION BY user_id 
                ORDER BY event_date
            ) * INTERVAL '1 day' AS grp
        FROM event_logs
    ) t
    GROUP BY user_id, grp
) t2
GROUP BY user_id;
