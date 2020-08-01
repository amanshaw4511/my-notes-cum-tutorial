-- GROUP BY --
	-- this clause is used to make same type of value in one row
	-- show total salary of employee of each name ( assuming all have distinct name)
	SELECT name,SUM(salary) from employee
	-- where ..........
	GROUP BY name;


-- HAVING CLAUSE --
	-- used with group by clause
	-- list all employee total salary > 30000
	SELECT name,SUM(salary) from employee
	GROUP BY name
	HAVING SUM(salary) > 30000 ;
