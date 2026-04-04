-- 3 months rolling average
WITH CTE AS (
    SELECT 
        DATE_TRUNC('month', order_date) AS month_date, 
        SUM(amount) AS total 
    FROM Orders
    GROUP BY 1
)
SELECT 
    TO_CHAR(month_date, 'MM-YYYY') AS order_month, -- Format for display here
    AVG(total) OVER (
        ORDER BY month_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_average 
FROM CTE
ORDER BY month_date;