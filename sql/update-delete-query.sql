-- UPDATE --
	-- change branch and roll of student	
	UPDATE students
	SET branch = 'cs', roll = 21 
	WHERE id = 1;
	-- note without where it will change all students branch to cs and roll to 21

-- DELETE --
	-- delete student with id = 4 from table
	DELETE FROM students
	WHERE id = 4 ;
	-- note without where it will delete all students from table leaving table empty


