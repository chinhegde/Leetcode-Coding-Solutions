-- 1070. Product Sales Analysis III
-- https://leetcode.com/problems/product-sales-analysis-iii/description/


with first_sale as (
    select product_id, min(year) as first
    from sales
    group by product_id
)

select s.product_id, s.year as first_year, quantity, s.price
from sales s inner join first_sale f on s.product_id = f.product_id
where s.year = f.first