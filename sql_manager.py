
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os 

dbname = "stock_data"

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')

con = None
con = connect(dbname='postgres', user=db_user, host='localhost', password=db_pass) #change to ini file 

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()

print("PostgreSQL server information")
print(con.get_dsn_parameters(), "\n")


cur.close()
con.close()
