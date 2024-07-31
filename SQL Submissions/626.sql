-- https://leetcode.com/problems/exchange-seats/

select id,
case 
when mod(id, 2) != 0 and lead(id) over (order by id asc) is not null then lead(student) over (order by id asc)
when mod(id, 2) = 0 then lag(student) over (order by id asc) 
else student
end as student
from seat