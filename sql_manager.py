
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2
import configparser


def config(section,filename='database.ini',):
    parser = configparser.ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


dbParams = config("postgresql")

con = psycopg2.connect(**dbParams)
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)


cur = con.cursor()




aaa = "select * from stock_fact2"
b ="""
SELECT count(*) FROM stock_fact2;
"""
cur.execute(b)

print(cur.fetchall())

cur.close()
con.close()


