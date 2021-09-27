
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

def connect_to_database():
    try:
        dbParams = config("postgresql")
        con = psycopg2.connect(**dbParams)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)   
        return con
    except:
        print ("I am unable to connect to the database")


def take_last_date_gpw(table_name:str=None) -> str:
    """
    take last date from 
    """
    con = connect_to_database()
    cur = con.cursor()
    
    query =f"select distinct date from {table_name} order by date desc limit 1;"
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    data = data[0][0].strftime("%d/%m/%Y")
    return data


if __name__ == "__main__":
    #a = take_last_date_gpw("gpw_facts")[0].strftime("%d/%m/%Y")
    #print(a)
    pass