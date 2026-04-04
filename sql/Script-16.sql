SELECT 
    stock_name,
    (sell_total - buy_total) AS net_gain_loss
FROM (
    SELECT 
        stock_name,
        SUM(CASE WHEN operation = 'Buy' THEN price ELSE 0 END) AS buy_total,
        SUM(CASE WHEN operation = 'Sell' THEN price ELSE 0 END) AS sell_total
    FROM stocks
    GROUP BY stock_name
) AS subquery
ORDER BY net_gain_loss DESC;