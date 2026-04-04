WITH CTE AS (
    SELECT person, unnest(string_to_array(basket, ',')) AS fruit 
    FROM baskets 
)
SELECT 
    person,
    CASE WHEN MAX(CASE WHEN fruit = 'Apple' THEN 1 ELSE 0 END) = 1 THEN 'Yes' ELSE 'No' END AS Apple,
    CASE WHEN MAX(CASE WHEN fruit = 'Mango' THEN 1 ELSE 0 END) = 1 THEN 'Yes' ELSE 'No' END AS Mango,
    CASE WHEN MAX(CASE WHEN fruit = 'Orange' THEN 1 ELSE 0 END) = 1 THEN 'Yes' ELSE 'No' END AS Orange,
    CASE WHEN MAX(CASE WHEN fruit = 'Guava' THEN 1 ELSE 0 END) = 1 THEN 'Yes' ELSE 'No' END AS Guava,
    CASE WHEN MAX(CASE WHEN fruit = 'Cherry' THEN 1 ELSE 0 END) = 1 THEN 'Yes' ELSE 'No' END AS Cherry
FROM CTE
GROUP BY person
ORDER BY person;

/*
with CTE as(
select person,unnest(string_to_array(basket,',')) as fruit from baskets )

select person,
 max(case when fruit='Apple' then 'Yes' else 'No' end) as Apple,
 max(case when fruit='Mango' then 'Yes' else 'No' end) as Mango,
 max(case when fruit='Orange' then 'Yes' else 'No' end) as Orange,
 max(case when fruit='Guava' then 'Yes' else 'No' end) as Guava,
 max(case when fruit='Cherry' then 'Yes' else 'No' end) as Cherry
 from CTE
 group by person
order by person*/