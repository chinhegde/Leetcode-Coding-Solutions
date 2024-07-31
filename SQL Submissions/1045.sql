-- https://leetcode.com/problems/customers-who-bought-all-products/

select customer_id
from customer c
group by customer_id
having count(distinct product_key) = (
    select count(*) from product
)