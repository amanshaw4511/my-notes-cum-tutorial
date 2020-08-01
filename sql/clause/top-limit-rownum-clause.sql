-- TOP --
	-- show top 5 students of class 9
	SELECT TOP 5 * FROM students
	WHERE class = 9;

	-- show top 10% students of university
	SELECT TOP 10% * FROM students;

-- LIMIT -- ( SUPPORTED BY MYSQL )
	SELECT * FROM students
	LIMIT 3;

-- ROWNUM -- ( SUPPORTED BY ORACLE )
	SELECT * FROM students
	WHERE ROWNUM <= 3;
