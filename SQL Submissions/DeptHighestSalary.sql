select Department, Employee, Salary
from
(select d.name Department, e.name Employee, e.salary Salary, 
dense_rank() over(partition by d.id order by e.salary desc) as r
from department d join employee e on d.id = e.departmentId) as t
where r = 1