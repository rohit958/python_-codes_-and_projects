WITH duplicates AS (
    SELECT 
        ctid,
        ROW_NUMBER() OVER (
            PARTITION BY budget_level 
            ORDER BY ctid
        ) AS rn
    FROM budgets
)
DELETE FROM budgets
WHERE ctid IN (
    SELECT ctid FROM duplicates WHERE rn > 1
);