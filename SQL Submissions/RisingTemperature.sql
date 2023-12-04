# Write your MySQL query statement below

# select id
# from (select *, lag(temperature,1) over(order by recordDate asc) as prevTemp 
#      from weather) k
# where temperature > prevTemp

select a.id
from weather a, weather b
where a.temperature > b.temperature
and datediff(a.recordDate,b.recordDate) = 1