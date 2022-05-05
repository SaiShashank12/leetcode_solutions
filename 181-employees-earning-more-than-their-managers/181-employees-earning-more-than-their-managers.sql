# Write your MySQL query statement below
select e2.name as Employee
from 
employee e1,
employee e2
where 
e1.Id=e2.ManagerId
and e1.salary<e2.salary