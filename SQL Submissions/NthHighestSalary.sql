CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select salary 
      from (
        select salary, dense_rank() over(order by salary desc) as r
        from employee
      ) t
      where r = N
      limit 1
  );
END