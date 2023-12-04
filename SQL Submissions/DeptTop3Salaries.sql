select Department, Employee, Salary
from (select d.name Department, e.name Employee, e.salary Salary, dense_rank() over(partition by d.id order by e.salary desc) r
from employee e join department d on d.id = e.departmentid
) as t
where r < 4
