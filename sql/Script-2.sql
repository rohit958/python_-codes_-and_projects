select * from dim_customer dc ;
select * from fact_sales ;



TRUNCATE TABLE stg_customer;

INSERT INTO stg_customer VALUES
(101, 'John Smith', 'Mumbai', 'Maharashtra', '2024-03-10'),  -- City changed
(102, 'Priya Patel', 'Bangalore', 'Karnataka', '2024-03-10'), -- No change
(104, 'Neha Sharma', 'Hyderabad', 'Telangana', '2024-03-10'); -- New customer

UPDATE dim_customer d
SET end_date = s.load_date - INTERVAL '1 day',
    is_current = FALSE
FROM stg_customer s
WHERE d.customer_id = s.customer_id
  AND d.is_current = TRUE
  AND (
       d.customer_name <> s.customer_name
    OR d.city <> s.city
    OR d.state <> s.state
  );

INSERT INTO dim_customer (customer_id, customer_name, city, state, start_date, end_date, is_current)
SELECT 
    s.customer_id, s.customer_name, s.city, s.state,
    s.load_date, NULL, TRUE
FROM stg_customer s
LEFT JOIN dim_customer d
    ON s.customer_id = d.customer_id
   AND d.is_current = TRUE
WHERE d.customer_id IS NULL
   OR (
       d.customer_name <> s.customer_name
    OR d.city <> s.city
    OR d.state <> s.state
   );



TRUNCATE TABLE stg_customer;
INSERT INTO stg_customer VALUES
(101, 'John Smith', 'Mumbai', 'Maharashtra', '2024-04-01'),
(102, 'Priya Patel', 'Chennai', 'Tamil Nadu', '2024-04-01'),
(103, 'Amit Verma', 'Delhi', 'Delhi', '2024-04-01'),
(104, 'Neha Sharma', 'Hyderabad', 'Telangana', '2024-04-01');

update dim_customer d 
set end_date = s.load_date , is_current=false
from stg_customer s where
d.customer_id = s.customer_id
and d.is_current = True
and (d.city <> s.city or 
	d.customer_name <> s.customer_name
	or d.state <> s.state)
	
	
insert into dim_customer (customer_id, customer_name, city, state, start_date, end_date, is_current)
select 
	s.customer_id, s.customer_name , s.city, s.state, s.load_date, null,  true 
	from stg_customer s
	left join dim_customer d on
	d.customer_id = s.customer_id 
	and d.is_current = True
	WHERE d.customer_id IS NULL
   OR (
       d.customer_name <> s.customer_name
    OR d.city <> s.city
    OR d.state <> s.state
   );



   );