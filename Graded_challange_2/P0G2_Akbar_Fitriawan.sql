/* 1. Buat Database */
-- CREATE DATABASE "GC2"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LOCALE_PROVIDER = 'libc'
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- TCL
BEGIN;

-- DDL 
CREATE TABLE segment(
	seg_id varchar(50) PRIMARY KEY NOT NULL,
	segment varchar(50) 
);

CREATE TABLE country(
	country_id varchar(10) PRIMARY KEY NOT NULL,
	country varchar(100) 
);

CREATE TABLE discount_band(
	disb_id varchar(20) PRIMARY KEY NOT NULL,
	discount_band varchar(50)
);

CREATE TABLE product(
	pro_id varchar(20) PRIMARY KEY NOT NULL,
	product varchar(50),
	manufacturing_price NUMERIC
);

CREATE TABLE main(
	seg_id varchar(50) NOT NULL,
	country_id varchar(50) NOT NULL,
	pro_id varchar(50) NOT NULL,
	disb_id varchar(50) NOT NULL,
	trans_id serial,
	sale_price numeric,
	units_sold numeric,
	profit numeric,
	tanggal date,
	primary key(trans_id),
	constraint fk_segment
		FOREIGN KEY(seg_id) references segment(seg_id),
	constraint fk_country
		FOREIGN Key(country_id) references country(country_id),
	constraint fk_product
		FOREIGN key(pro_id) references product(pro_id),
	constraint fk_disb
		FOREIGN key(disb_id) references discount_band(disb_id)
);

SAVEPOINT acc;

COPY segment(seg_id,segment)
FROM 'C:\temp\segment.csv'
DELIMITER ','
CSV HEADER;



COPY country(country_id,country)
FROM 'C:\temp\country.csv'
DELIMITER ','
CSV HEADER;

COPY discount_band(disb_id,discount_band)
FROM 'C:\temp\discount_band.csv'
DELIMITER ','
CSV HEADER;

COPY product(pro_id,product,manufacturing_price,units_sold)
FROM 'C:\temp\product.csv'
DELIMITER ','
CSV HEADER;

SAVEPOINT acc2;


COPY main(seg_id,country_id,pro_id,disb_id,trans_id,sale_price,units_sold,profit,tanggal)
FROM 'C:\temp\main.csv'
DELIMITER ','
CSV HEADER;

SAVEPOINT acc3;

-- Create User--
Create User jhin with password '4444';

Create user ashe with password 'felyord';

create user ezriel with password 'ezz';

SELECT * FROM pg_user;

-- Pemberian akses query --
grant select on main to ashe;

ROLLBACK to savepoint acc3;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO jhin;

GRANT ALL PRIVILEGES ON product TO ezriel;

SAVEPOINT acc4;

-- DML --
select * from segment;
select * from product;
select * from discount_band;
select * from country;
select * from main;

/* Masukan data indonesia dan china*/
insert into country (country_id, country)
values ('C106','Indonesia'),
		('C107','India')

/* update data 'India' jadi 'China'*/
update country 
set country = 'China'
where country_id = 'C107';

/* hapus negara dimana nama indonesia */
DELETE from country 
where country = 'Indonesia';

ROLLBACK to savepoint acc4;

SAVEPOINT acc4;

-- 5.1 Pengujian database --

select * from main;

select 
count(profit) as total_count
from main;

/* total profit */
SELECT
	seg_id,
	sum(profit) as total_profit
from main
where disb_id != 'D41'
group by seg_id;

/* informasi statistik */
SELECT 
    country_id,
    AVG(sale_price) AS rata_rata_sales,
    MIN(sale_price) AS min_sales,
    MAX(sale_price) AS max_sales
FROM 
    main
GROUP BY 
    country_id;


ROLLBACK to savepoint acc4;
COMMIT;








