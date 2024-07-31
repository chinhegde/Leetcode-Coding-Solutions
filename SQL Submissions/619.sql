-- https://leetcode.com/problems/biggest-single-number/

select ifnull((
    select num
    from MyNumbers
    group by num
    having count(num) < 2
    order by 1 desc
    limit 1), null) as num