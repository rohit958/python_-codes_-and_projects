Steps in cleaning Data-
SQL v/s Pyspark dataframes

1. removing dulplicates

SQL: -- two methods 
(i).using group by
SELECT column1, column2
FROM table_name
group by column1, column2;

or 
(ii).select DISTINCT ID from table;

(iii).select *, row_number() over(partition by id) as rn from employee
where rn <1

Pyspark:
df.dropDuplicates()
-----------------------------------------------------------------------------------------------------------------------------------
2. handling missing values or replacing null values with default value

select count(*) from employee where id is not null -- getiing number of Null rows
or
--replace null value with default
select coalesce("ID","default value") from emp;

pyspark-
df.na.drop('ID')

# number of null rows in Pyspark
df1= df.select([count(when(col(i).isNull(),i)).alias(i) for i in df.columns])
df1.show()

replace null values with default
1.df1=df.fillna({"email": "unknown"})

2.df_filled = df.withColumn("email", coalesce(col("email"),lit("unknown")))

-----------------------------------------------------------------------------------------------------------------------------------
3. date format issue
pyspark=df.withColumn("date",to_date(col("date")))

SQL= select cast('2024-08-01' as DATE) from employee

update employee
set datecol = cast (datecol as Date)
-----------------------------------------------------------------------------------------------------------------------------------
4. Substring checks

-- Using LIKE operator
SELECT * FROM customers
WHERE customer_name LIKE '%Smith%';

-- Using CHARINDEX (SQL Server)
SELECT * FROM customers
WHERE CHARINDEX('Smith', customer_name) > 0;

-- Using LOCATE (MySQL)
SELECT * FROM customers
WHERE LOCATE('Smith', customer_name) > 0;

pyspark-
df.filter(col("name").like("%John%")).show()

df.filter(col("city").rlike("Los.*")).show()


-----------------------------------------------------------------------------------------------------------------------------------
5. standardising
--replacing null values with average one 


select coalesce(salary,(select avg(salary) from employees)) from employees

mean_age = df.select(F.mean(col("age"))).collect()[0][0]

df_filled = df.withColumn("age", when(col("age").isNull(), mean_age).otherwise(col("age")))

-----------------------------------------------------------------------------------------------------------------------------------

6:Validation
-- Validating data against predefined rules or constraints helps ensure data integrity. SQL constraints like NOT NULL, UNIQUE, or CHECK can be used during table creation or alteration.
Example:
CREATE TABLE table_name (
 column1 INT NOT NULL UNIQUE,
 column2 VARCHAR(50) CHECK (column2 IN ('value1', 'value2')),
 ..);
 
 -----------------------------------------------------------------------------------------------------------------------------------
 7.removing special characters
 
 SELECT column_name, REPLACE(column_name, '[^a-zA-Z0-9]', '') AS cleaned_column
FROM your_table;

pyspark-
df.select(regexp_replace(col("email"),r"[^a-zA-Z0-9]","")).show()

-----------------------------------------------------------------------------------------------------------------------------------

8. removing white spaces
--we can use
--trim()-removes whitepsaces from both ends
--RTRIM()-removes whitepsaces from right
--LTRIM()-removes whitepsaces from left

select trim(Address) from employee;

pyspark-
df.select(trim(col("Adress")).show()