-- https://leetcode.com/problems/market-analysis-i/

select u.user_id as buyer_id, join_date, ifnull(orders_in_2019, 0) as orders_in_2019
from users u left join (
    select buyer_id, 
    ifnull(count(distinct order_id), 0) as orders_in_2019 
    from orders
    where year(order_date) = 2019
    group by 1) as temp 
on u.user_id = temp.buyer_id
