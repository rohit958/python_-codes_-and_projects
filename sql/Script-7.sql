/*
 * input
 * 1
 * 2
 * 3
 * 4
 * 5
 * 
 * expected output
 * 
 * 1
 * 2
 * 2
 * 3
 * 3
 * 3
 * 4
 * 4
 * 4
 * 4
 * 5
 * 5
 * 5
 * 5
 * 5
 * */


--cross join
select n1.n from numbers n1 ,numbers n2
where n1.n>=n2.n


--self join
select n1.n from numbers n1 join numbers n2
on n1.n>=n2.n

