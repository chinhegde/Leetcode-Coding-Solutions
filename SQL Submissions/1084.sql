-- https://leetcode.com/problems/sales-analysis-iii/

select distinct p.product_id, p.product_name
from product p join sales s on s.product_id = p.product_id
where (sale_date >= '2019-01-01' and sale_date <= '2019-03-31')
and p.product_id not in (
    select distinct product_id 
    from sales 
    where sale_date < '2019-01-01' or sale_date > '2019-03-31'
    )
