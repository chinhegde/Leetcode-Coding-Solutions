/* Write your T-SQL query statement below */

SELECT user_id, concat(UPPER(LEFT(name, 1)),LOWER(RIGHT(name,len(name)-1))) as name
from Users
order by user_id