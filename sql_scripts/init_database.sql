CREATE TABLE IF NOT EXISTS public.stock_fact4
(
    date date,
    symbol character varying(50) COLLATE pg_catalog."default",
    "ISIN" character varying(50) COLLATE pg_catalog."default",
    currency character varying(3) COLLATE pg_catalog."default",
    open numeric,
    max numeric,
    min numeric,
    close numeric,
    "%change" numeric,
    quantity integer,
    num_of_trans integer,
    volume numeric,
    num_of_o_pos integer,
    vol_of_o_pos integer,
    nominal_price integer
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.stock_dimension" (
	"stick_id" serial NOT NULL,
	"stock_name" serial(30) NOT NULL,
	"stock_currency" varchar(3) NOT NULL,
	CONSTRAINT "stock_dimension_pk" PRIMARY KEY ("stick_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.company_dimension" (
	"company_id" serial NOT NULL,
	"company_ticket" serial(10) NOT NULL,
	"company_name" serial(50) NOT NULL,
	CONSTRAINT "company_dimension_pk" PRIMARY KEY ("company_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.FinInst_dimension" (
	"finInst_id" serial,
	"finInst_name" serial(100),
	CONSTRAINT "FinInst_dimension_pk" PRIMARY KEY ("finInst_id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "stock_fact" ADD CONSTRAINT "stock_fact_fk0" FOREIGN KEY ("company_id") REFERENCES "company_dimension"("company_id");
ALTER TABLE "stock_fact" ADD CONSTRAINT "stock_fact_fk1" FOREIGN KEY ("stock_id") REFERENCES "stock_dimension"("stick_id");
ALTER TABLE "stock_fact" ADD CONSTRAINT "stock_fact_fk2" FOREIGN KEY ("finInst_id") REFERENCES "FinInst_dimension"("finInst_id");








