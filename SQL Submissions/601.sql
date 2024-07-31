-- https://leetcode.com/problems/human-traffic-of-stadium/

-- SOLUTION 1:

with temp as (
    select id, 
    visit_date, 
    people
    from stadium 
    where people >= 100
    )

select id, visit_date, people
from temp
where 
    ((id + 1) in (select id from temp) AND
    (id + 2) in (select id from temp)) OR
    ((id - 1) in (select id from temp) AND
    (id + 1) in (select id from temp)) OR
    ((id - 1) in (select id from temp) AND
    (id - 2) in (select id from temp)) 

order by visit_date;

-- SOLUTION 2

with temp as (
    select id, 
    visit_date, 
    people, 
    case when people >=100 and lead(people) over (order by id asc) >= 100 then lead(id) over (order by id asc)
    else Null end as id1,
    case when people >=100 and lead(people, 2) over (order by id asc) >= 100 then lead(id, 2) over (order by id asc)
    else Null end as id2
    from stadium
    )

select id, visit_date, people 
from temp
where id in (
    select id from temp 
    where id1 is not Null and id2 is not Null
    union
    select id2 from temp
    where id1 is not Null and id2 is not Null
    union
    select id1 from temp
    where id1 is not Null and id2 is not Null
)
order by visit_date;


