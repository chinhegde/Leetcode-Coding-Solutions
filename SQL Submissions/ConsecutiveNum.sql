select distinct num as ConsecutiveNums
from (
  select num, 
  lag(num) over(order by id) as prev_num,
  lead(num) over(order by id) as next_num
  from logs
) as t
where prev_num = num and num = next_num