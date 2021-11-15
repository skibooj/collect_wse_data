import pandas as pd
from datetime import datetime

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
    dates_to_download = range_of_dates.strftime("%d-%m-%Y").tolist() 
    return dates_to_download
  
 
