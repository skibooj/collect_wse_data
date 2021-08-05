insert into
stock_facts (date,
			 comp_id,
			 stock_id,
			 instrument_id,
			 open_price,
			 max_price,
			 min_price,
			 close_price,
			 price_change_perc,
			 volume,
			 transactions_number)
Values (now(), 1,2,3,4,5,6,6,3,3,4);




select * from stock_facts;


-- creating database


CREATE TABLE "public".companies_dimension
(
 comp_id     int NOT NULL,
 symbol      varchar(25) NOT NULL,
 companyName varchar(50) NOT NULL,
 CONSTRAINT PK_gpw_stock_inc PRIMARY KEY ( comp_id )
);

--

CREATE TABLE "public".financial_instrument_id
(
 instrument_id int NOT NULL,
 fin_ins_name  varchar(50) NOT NULL,
 CONSTRAINT PK_financial_instrument_id PRIMARY KEY ( instrument_id )
);



CREATE TABLE "public".stock_dimension
(
 stock_id       int NOT NULL,
 stock_name     varchar(50) NOT NULL,
 stock_currency varchar(50) NOT NULL,
 CONSTRAINT PK_stock_dimension PRIMARY KEY ( stock_id )
);




CREATE TABLE "public.stock_fact" (
	"dupa" DATE NOT NULL,
	"stock_id" int NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.stock_dimension" (
	"stick_id" serial NOT NULL,
	"stock_name" serial(30) NOT NULL,
	CONSTRAINT "stock_dimension_pk" PRIMARY KEY ("stick_id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "stock_fact" ADD CONSTRAINT "stock_fact_fk0" FOREIGN KEY ("stock_id") REFERENCES "stock_dimension"("stick_id");







