import pandas as pd
from datetime import datetime
import shutil
import zipfile
import glob 

def current_date()-> str:
    today = pd.to_datetime("today").strftime("%d-%m-%Y")
    return today


def list_of_dates(period_start: str = None,period_end: str = None) -> list:
    """
    data shoud have format: dd/mm/yyyy
    """
    
    ps = datetime.strptime(period_start, "%d/%m/%Y").strftime("%m-%d-%Y")
    pe = datetime.strptime(period_end, "%d/%m/%Y").strftime("%m-%d-%Y")
    
    # freq argument is a constant because stock exchange work only in a workdays
    range_of_dates=pd.date_range(start=ps,end=pe,freq="B")
    range_of_dates=pd.to_datetime(range_of_dates)
    #dates_to_download = range_of_dates.strftime("%d-%m-%Y").tolist() 
    return list(range_of_dates)


def move_to_archive(output_path:str=None,dir_name:str=None) -> None:
    shutil.make_archive(output_filename, 'zip', dir_name)
   

def clear_directory():
    pass

 

if __name__ == "__main__":
    a = list_of_dates(period_start='01/11/2021',period_end='15/11/2021')
    print(len(a))
      
