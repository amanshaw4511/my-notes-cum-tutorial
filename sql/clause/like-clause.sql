-- LIKE --
	-- used to compare similer value using wildcard opertors
		-- (%) : represents zero or more characters
		-- (_) : represents one number or characters


	-- select movies name start with 'The'
	SELECT title FROM movies
	WHERE title LIKE 'The%';

	-- select movies name contains 'man'
	SELECT title FROM movies
	WHERE title LIKE '%man%';

	-- select students name 4 letters start with 'a' and end wih 'n'
	SELECT * FROM students
	WHERE name LIKE 'a__n';


