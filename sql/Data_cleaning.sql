Steps in cleaning Data-
1. removing dulplicates

SQL: -- two methods 
(i).using group by
SELECT column1, column2
FROM table_name
group by column1, column2;

or 
select DISTINCT ID from table;

select *, row_number() over(partition by id) as rn from employee
where rn <1

Pyspark:
df.dropDuplicates()
-----------------------------------------------------------------------------------------------------------------------------------
2. handling missing values or replaceing null values with default value

select * from employee where id is not null

select coalesce("ID","default value") from emp;

df.na.drop('ID')

-----------------------------------------------------------------------------------------------------------------------------------
3. date format issue
pyspark=df.withColumn("date",to_date(col("date")))

SQL= select cast('2024-08-01' as DATE) from employee

update employee
set datecol = cast (datecol as Date)
-----------------------------------------------------------------------------------------------------------------------------------
4. removing outliners


-----------------------------------------------------------------------------------------------------------------------------------
5. standardising
removing discrete values with average one or bring into 1-10 scale eg sal= sal/max(sal)

6: Validating data against predefined rules or constraints helps ensure data integrity. SQL constraints like NOT NULL, UNIQUE, or CHECK can be used during table creation or alteration.
Example:
CREATE TABLE table_name (
 column1 INT NOT NULL UNIQUE,
 column2 VARCHAR(50) CHECK (column2 IN ('value1', 'value2')),
 ..);
 
 7.removing special characters
 
 SELECT column_name, REPLACE(column_name, '[^a-zA-Z0-9]', '') AS cleaned_column
FROM your_table;