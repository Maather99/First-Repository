
create table courses(
c_id char(8) CONSTRAINT c_courseid_pk primary key,
c_name varchar(20));

create table Students(
s_id int CONSTRAINT s_studentid_pk primary key,
s_first_name varchar(30),
s_last_name varchar(30),
s_email varchar(50),
s_mobile_no varchar(10),
s_gender char(1),
s_fees numeric(8,2),
course_id char(8),
CONSTRAINT student_course_fk FOREIGN KEY(course_id) REFERENCES courses(c_id) 
);

select* from courses ;


INSERT INTO Students(s_id, s_first_name, s_last_name, s_email, s_mobile_no, s_gender, s_fees) VALUES (2,'maather','alriyami','maather@gmail.com',92390141,'f',50);


SELECT TABLE_NAME,CONSTRAINT_TYPE,CONSTRAINT_NAME 
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTs
WHERE TABLE_NAME = 'Students';


ALTER TABLE Students DROP CONSTRAINT student_course_fk; 

ALTER TABLE Students ADD CONSTRAINT student_course_fk FOREIGN KEY(course_id) REFERENCES courses(c_id) ;

INSERT INTO courses VALUES (2, '');
INSERT INTO courses VALUES (4, NULL);
select* from courses ;

SELECT SYSDATETIME();



create table c1(
c_id char(8)  primary key,
c_name varchar(20));

create table c2(
c_id char(8) primary key,
c_name varchar(20));

INSERT INTO c1(c_id,c_name) VALUES (4,'AHMED');

INSERT INTO c2(c_id,c_name)
SELECT c_id, c_name FROM c1;

select* from c2 ;

UPDATE c1
SET  c_id =3;
select* from c1 ;

create table products(
product_id char(8) primary key,
price numeric(20));


create table Product(
product_id int primary key,
product_name varchar(20),
quantity int,
price numeric(8,2)
);


INSERT INTO Product(product_id,product_name,quantity,price) VALUES (4,'p22',2,100);
INSERT INTO Product(product_id,product_name,quantity,price) VALUES (5,'p32',6,150);

select* from Product ;
select quantity*price from Product as total_price where product_name ='p22';

BEGIN TRANSACTION
UPDATE Product SET quantity = 2 WHERE product_name ='p22';

ROLLBACK;

select sum(price) as total_pprice from Product;
