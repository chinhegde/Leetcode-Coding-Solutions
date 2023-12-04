/* Write your T-SQL query statement below */

select customer_id, count(*) count_no_trans
from visits 
where visit_id not in (select visit_id from transactions)
group by customer_id
order by 2 desc,1 asc