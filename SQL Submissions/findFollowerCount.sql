/* Write your T-SQL query statement below */

select user_id, count(distinct follower_id) followers_count
from followers
group by user_id