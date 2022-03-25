-- create database smart_trolley;
use smart_trolley;

create table coordinates_table(location varchar(10));
insert into coordinates_table value("a-1-1");
select * from coordinates_table;
delete from coordinates_table;
SET SQL_SAFE_UPDATES = 0; 