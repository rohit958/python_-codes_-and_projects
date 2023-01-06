--sql
--concat alternative
SELECT Name || '(' || SUBSTR(Occupation, 1, 1) || ')'
FROM OCCUPATIONS
ORDER BY Name;

SELECT 'There are a total of ' || Count(Name) || ' ' || LOWER(Occupation) || 's.'
FROM Occupations
GROUP BY Occupation
ORDER BY Count(Name), Occupation;


----------------------------------------------------------------------------


---pivot TABLE
/*
You can use the PIVOT and UNPIVOT relational operators to change a table-valued expression into another table. 
PIVOT rotates a table-valued expression by turning the unique values from one column in the expression into multiple columns in the output. 
And PIVOT runs aggregations where they're required on any remaining column values that are wanted in the final output. 
UNPIVOT carries out the opposite operation to PIVOT by rotating columns of a table-valued expression into column values.*/

SELECT
    [Doctor], [Professor], [Singer], [Actor]
FROM
(
    SELECT ROW_NUMBER() OVER (PARTITION BY OCCUPATION ORDER BY NAME) [RowNumber], * FROM OCCUPATIONS--partioning
) AS tempTable
PIVOT --pivoting
(
    MAX(NAME) FOR OCCUPATION IN ([Doctor], [Professor], [Singer], [Actor])
) AS pivotTable


----------------------------------------------------------------------------


/*Row number function is a window function that assigns a sequential integer to each row within the partition of a result set.
 The row number starts with 1 for the first row in each partition.
 */
 
 ROW_NUMBER() OVER (
    [PARTITION BY partition_expression, ... ]
    ORDER BY sort_expression [ASC | DESC], ...
)

/*
PARTITION BY
The PARTITION BY clause divides the result set into partitions (another term for groups of rows). The ROW_NUMBER() function is applied to each partition separately and reinitialized the row number for each partition.

The PARTITION BY clause is optional. If you skip it, the ROW_NUMBER() function will treat the whole result set as a single partition.

ORDER BY
The ORDER BY clause defines the logical order of the rows within each partition of the result set. The ORDER BY clause is mandatory because the ROW_NUMBER() function is order sensitive.
*/


----------------------------------------------------------------------------

--*traingle with SQL CODE
***** --from 20
****
***
**
*

SELECT REPEAT('* ', @NUMBER := @NUMBER - 1) --mysql
FROM information_schema.tables, (SELECT @NUMBER:=21) t LIMIT 20

DECLARE @i INT = 20 --mysql
WHILE (@i > 0) 
BEGIN
   PRINT REPLICATE('* ', @i) 
   SET @i = @i - 1
END


select rpad('*', x,' *') from  --oracle sql
( SELECT LEVEL x FROM DUAL CONNECT BY LEVEL <= 40 Order by Level desc ) where mod(x,2) = 0;

----------------------------------------------------------------------------

--*traingle with SQL CODE
*
**
***
****
*****--upto 20

SELECT REPEAT('* ', @NUMBER := @NUMBER + 1) --mysql
FROM information_schema.tables, (SELECT @NUMBER:=0) t LIMIT 20;

----------------------------------------------------------------------------

--prime numbers upto 1000 

--select all the numbers till 1000 in the tblnums
with recursive tblnums
as (
	select 2 as nums
	union all
	select nums+1 
	from tblnums
	where nums<1000)
	
select group_concat(tt.nums order by tt.nums separator '&')  as nums
from tblnums tt
where not exists 
	#the num should not be divisible by any number less than it
	( select 1 from tblnums t2 
	where t2.nums <= tt.nums/2 and mod(tt.nums,t2.nums)=0) 
	
--------------------------------------------------------------------------------------------------------------------------------------------------------	
/*
	
			JOIN																									UNION
JOIN combines data from many tables based on a matched condition between them.			SQL combines the result-set of two or more SELECT statements.
It combines data into new columns.														It combines data into new rows
Number of columns selected from each table may not be same.								Number of columns selected from each table should be same.
Datatypes of corresponding columns selected from each table can be different.			Datatypes of corresponding columns selected from each table should be same.
It may not return distinct columns.														It returns distinct rows.
*/
--------------------------------------------------------------------------------------------------------------------------------------------------------