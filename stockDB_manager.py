
from pandas.core.frame import DataFrame
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2
import configparser
import pandas as pd

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


def take_last_date(stock_name:str=None) -> str:
    """
    take last dowloaded date for certain stock name
    """
    con = connect_to_database()
    cur = con.cursor()
    
    query =f"select distinct date from stock.{stock_name} order by date desc limit 1;"
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    data = data[0][0].strftime("%d/%m/%Y") #fetchall data is a nested tuple in a list
    return data


def bulk_insert(file_path:str = None,table_name:str=None):
    con = connect_to_database()
    cur = con.cursor()   
    query = f"""
            COPY {table_name}
            FROM '{file_path}' 
            DELIMITER ',' 
            CSV HEADER;
            """
    cur.execute(query)
    con.close()
    pass


def select_gpw_data() -> DataFrame:
    query = """
    select * from stock.stg_gpw;
    """
    con = connect_to_database()
    data = pd.read_sql_query(query,con)
    return data


def get_holidays(stock_name) -> DataFrame:
    query = f"""select holiday from stock_holiday where stock_name = "{stock_name}";"""
    con = connect_to_database()
    data = pd.read_sql_query(query,con)
    return data

if __name__ == "__main__":
    #demo
    a = select_gpw_data()
    print(a)
    pass
