-- name starts with A 
select * from customers_test
where name ~'A'

--name not start with A
select * from customers_test
where name !~'A'

--ends with gmail.com
select * from customers_test
where email ~'@gmail.com$'

--starts with A or D
select * from customers_test
where name ~'^(A|D)'

--invalid emails
select * from customers_test
where email !~'@'

--name of 5 characters
select * from customers_test
WHERE name ~ '^\w{5}$';

--name contains digit
select * from customers_test 
where email ~'\w[0-9]'

--names end with a
select * from customers_test
where name ~*'a$'

--name not surname ends with a
select * from customers_test
where name ~'^[a-zA-Z]*a(\s|$)'

--email starts with vowels
select * from customers_test 
where email ~*'^[aeiou]'

--customers whose email not contain '@gmail.com' --practice 5
select * from customers_test
where email !~'@gmail.com'

-- customer have space--practice 6

select * from customers_test
where name ~'\s'

select * from customers_test 
where email !~* '[a-z0-9._%+-]*@[a-z0-9.-]+]*.[a-z]{2,}$';

--domain
select *, substring(email from '@(.*)$') as domain  from customers_test 

--also
select *, split_part(email,'@',2) as domain  from customers_test

--valid names
select * from customers_test 
where name !~'[^a-zA-Z0-9\s.]'

--clean name

select strip(name) from customers_test --option 1


select regexp_replace(name,'^\s+|\s+$','') from customers_test --option 2

--valid phone number
select * from customers_test 
where phone !~'^[0-9]{10}$'
 
select regexp_replace(phone,'[^0-9]','','g') from customers_test