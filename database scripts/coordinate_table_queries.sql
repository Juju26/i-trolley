-- create database smart_trolley;
use smart_trolley;

create table coordinates_table(location varchar(10));
insert into coordinates_table value("a-1-1");
select * from coordinates_table;
delete from coordinates_table;
SET SQL_SAFE_UPDATES = 0; 

-- alter table coordinates_table add x_cord double;
-- alter table coordinates_table add y_cord double;

alter table coordinates_table modify column x_cord float8;
alter table coordinates_table modify column y_cord float8;

update coordinates_table set x_cord='6.6666666'