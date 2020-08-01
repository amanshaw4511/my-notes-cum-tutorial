-- create table --
-- 	table name - define column - assign data type and constrains to columns
	CREATE TABLE students(
		student_id INT,
		name VARCHAR(20) NOT NULL,
		roll INT UNIQUE NOT NULL,
		PRIMARY KEY(student_id));

-- describe table --
	DESC students;

-- add column  --
	ALTER TABLE students
	ADD COLUMN marks INT ;

-- remove column --
	ALTER TABLE students
	DROP COLUMN marks;

-- modify column type
	ALTER TABLE students
	ALTER COLUMN marks NOT NULL;

-- drop table --
	DROP TABLE students;


-- insert into table --
-- 	only values
	INSERT INTO students
	VALUES ( 1, 'aman' , 01, 'electrical' );
--	column name - value
	INSERT INTO stuents ( id, roll, name )
	VALUES ( 2, 11 , 'ravi' );

-- populate one table using another --
	INSERT INTO students[( id, roll, name)]
	SELECT id, roll, name FROM students_old
	WHERE id <20 ;


