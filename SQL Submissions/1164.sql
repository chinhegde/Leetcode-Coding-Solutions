-- https://leetcode.com/problems/product-price-at-a-given-date/

with temp as (
    select 
        product_id, 
        new_price,
        rank() over (partition by product_id order by change_date desc) as rnk
    from products
    where change_date <= '2019-08-16')

select distinct product_id, new_price as price
from temp 
where rnk = 1

union 

select product_id, 10 as price
from products
where product_id not in (select distinct product_id from temp);