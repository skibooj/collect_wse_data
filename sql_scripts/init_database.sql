CREATE TABLE "public.stock_fact" (
	"date" DATE NOT NULL,
	"company_id" int NOT NULL,
	"stock_id" int NOT NULL,
	"finInst_id" int NOT NULL,
	"open_price" numeric(4) NOT NULL,
	"close_price" numeric(4) NOT NULL,
	"max_price" numeric(4) NOT NULL,
	"min_price" numeric(4) NOT NULL,
	"price_change_percentage" numeric(4) NOT NULL,
	"volume" int NOT NULL,
	"transactions" int NOT NULL
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








