-- show all table contents
	SELECT * FROM students;

-- show some column of table
	SELECT name,roll FROM students;

-- show students marks is more than 80
	SELECT name,roll FROM students
	WHERE marks > 80;

-- COUNT --
	-- no of students scored more then 80%
	SELECT COUNT(*) FROM students
	WHERE marks > 80;

-- AND --
	-- students from electrical marks more than 80
	SELECT name,roll FROM students
	WHERE marks > 80 AND brach = 'electrical';

-- OR --
	-- no of students in total electrical and cs
	SELECT COUNT(*) FROM students
	WHERE branch = 'electrical' OR branch = 'cs'

-- NOT --
	-- total students except cs
	SELECT COUNT(*) FROM students
	WHERE NOT bracnch = 'cs';


	
