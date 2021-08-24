
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os 

table_check = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND 
    schemaname != 'information_schema';
"""

table_check2 = """
 SELECT current_database();
"""


table_create = """
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
)
"""
dbname = "stock_data"


db_create = f"""
CREATE DATABASE {dbname}
"""

db_drop = f"DROP DATABASE {dbname}"

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')

con = None
con = connect(dbname='postgres', user=db_user, host='localhost', password=db_pass)


con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()

print("PostgreSQL server information")
print(con.get_dsn_parameters(), "\n")


cur.close()
con.close()
