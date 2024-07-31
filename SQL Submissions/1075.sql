-- https://leetcode.com/problems/project-employees-i/

select distinct p.project_id, 
round(avg(e.experience_years) over (partition by p.project_id), 2) as average_years
from project p join employee e on p.employee_id = e.employee_id
