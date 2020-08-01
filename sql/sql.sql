create database university;

create table students(
	student_id int primary key ,
	name varchar(20) not null,
	roll int not null unique default 'not decided',
	branch varchar(20)
);

drop table students;

describe students;

alter table students add marks decimal(4,2);

alter table students drop column marks;

select * from students;

insert into students( student_id, name, roll, branch)
	values( 1, 'aman', 1, 'electrical');

select name,roll from students
	where marks > 8.0 ;
-- < , > , <= , >=, = , <>, AND, OR

select * from students
	where name IN ('aman' , 'rahul', 'ravi');

select * from students
	where name IN ('aman', 'rahul', 'ravi') AND branch = 'electrical';


