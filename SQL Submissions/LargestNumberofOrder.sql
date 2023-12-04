/* Write your T-SQL query statement below */
select customer_number 
from (select customer_number, rank() over(order by count(distinct order_number) desc) t
     from orders
     group by customer_number) a
where t = 1
