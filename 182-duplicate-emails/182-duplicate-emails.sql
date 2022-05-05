# Write your MySQL query statement below
select email
from (select email,count(email)
      from person
      group by email
      having count(email)>1) em
      