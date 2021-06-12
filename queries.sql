/*Queries used during Debugging, Testing and Creating Schema.*/

/*create database munchin;
use munchin;
create table section(section_id int primary key auto_increment, section_name varchar(50));
create table class(class_id int primary key auto_increment, class_name varchar(50), section_id int not null,
    constraint fk1 foreign key (section_id) references section(section_id));
create table students(registration_no int unique not null, roll_no int primary key auto_increment not null, name varchar(30),
    email varchar(64),
    phone_no bigint check(phone_no <= 9999999999 and phone_no >= 1111111111),
    attendance int check(attendance <= 100 and attendance >= 0),
    class_id int, section int,
    constraint fk2 foreign key (class_id) references class(class_id),
    constraint fk3 foreign key (section) references section(section_id));
insert into section(section_id, section_name) values(1, "A"), (2, "B");
insert into class(class_id, class_name, section_id) values(1, "10th", 1), (2, "11th", 1), (3, "12th", 1), (4, "10th", 2);*/
/*select * from students;
select * from class;
select * from section;*/
set @rowindex:=1; select avg(d.attendance) as median from (select @rowindex:=@rowindex+1 as rowindex, students.attendance as attendance from students order by students.attendance) as d where d.rowindex in (floor(@rowindex/2), ceil(@rowindex/2));