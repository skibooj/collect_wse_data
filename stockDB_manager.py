
from pandas.core.frame import DataFrame
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2
import configparser
import pandas as pd
import numpy as np


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


def take_last_date(stock_name:str) -> str:
    """
    take last dowloaded date for certain stock name
    """
    con = connect_to_database()
    cur = con.cursor()
    
    query =f"""select f.date
		from fact_quotes as f join dim_stock as s on f.stock_id = s.stock_id
		where s.name = '{stock_name}'
		order by date desc 
		limit 1; """
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

def load_to_main_table(staging_table:str):
    con = connect_to_database()
    cur = con.cursor()   
    query = f"""
            INSERT INTO public.fact_quotes(
            date, stock_id, security_id, open, max, min, close, quantity, num_of_trans, volume)
            select
                stg.date
                ,stc.stock_id
                ,sec.security_id
                ,stg.open
                ,stg.max
                ,stg.min
                ,stg.close
                ,stg.quantity
                ,stg.num_of_trans
                ,stg.volume
                from {staging_table} as stg
            left JOIN dim_stock as stc on stg.stock_name = stc.name
            left JOIN dim_securities as sec on stg.isin = sec.isin and stg.symbol = sec.symbol
            """
    cur.execute(query)
    con.close()
    pass





def get_holidays(stock_name) -> DataFrame:
    query = f"""select dim_holidays.date from dim_holidays inner join dim_stock
                on dim_holidays.stock_id = dim_stock.stock_id
                where dim_stock.name = '{stock_name}';"""
    con = connect_to_database()
    data = pd.read_sql_query(query,con)
    data = data.astype({'date': 'datetime64[ns]'})
    return list(data['date'])


def execute_query(query:str):
    con = connect_to_database()
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    print(data)
    pass


def clear_table(table_name:str):
    con = connect_to_database()
    cur = con.cursor()
    query = f"delete from {table_name}"
    cur.execute(query)
    con.close()
    pass

def get_data_to_df(stock_name:str) -> DataFrame:
    query = f"""select dim_holidays.date from dim_holidays inner join dim_stock
                on dim_holidays.stock_id = dim_stock.stock_id
                where dim_stock.name = '{stock_name}';"""
    con = connect_to_database()
    data = pd.read_sql_query(query,con)
    
    return data

if __name__ == "__main__":
    execute_query(query="select count(*) from stg_gpw;")

