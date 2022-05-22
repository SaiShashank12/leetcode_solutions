# Write your MySQL query statement below
with temp as(
select
    name customer_name
    , c.customer_id
    , order_id
    , order_date
    , rank() over(partition by c.customer_id order by order_date desc) `rank`
from Customers c
    inner join Orders o
        on c.customer_id = o.customer_id
)
select
    customer_name
    , customer_id
    , order_id
    , order_date
from temp
where `rank` <= 3
order by customer_name, customer_id, order_date desc