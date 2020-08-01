-- ORDER BY --
	-- ASC
	-- students marks  less than 35 ( min to high )
	SELECT * FROM students
	WHERE marks < 35
	ORDER BY marks ASC;

	-- DESC (defualt)
	-- students marks greater than 80 ( max to low )
	SELECT * FROM students
	WHERE marks > 80
	ORDER BY marks;


	
