import pandas as pd
from pandas.core.base import DataError
import requests
import os.path



# settings that skip warnings about risky connection
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


# freq argument
def list_of_dates(period_start: str = None,period_end: str = None) -> list:
    range_of_dates=pd.date_range(start=period_start,end=period_end,freq="B") 
    dates_to_download = range_of_dates.strftime("%Y-%m-%d").tolist() 
    return dates_to_download



def download_gpw1(
    dates_list: list=None,
    financial_instument: str=None):
    
    """
    Download excel files to D_data folder and create seperate folder for current financial instrument 
    
    return: None
    """
    source_path = os.path.dirname(os.path.abspath(__file__))
    final_directory = f"{source_path}/D_data/{financial_instument}"
    
    if not os.path.exists(final_directory):
        os.mkdir(final_directory)


    for each_date in dates_list:
        url = f"https://www.gpw.pl/archiwum-notowan?fetch=1&type={financial_instument}&instrument=&date={each_date}"
        resp = requests.get(url, verify=False)
        file_name = each_date
        with open(f"{final_directory}/{file_name}.xls", 'wb') as output:
                output.write(resp.content) 
    pass
 


if __name__ == "__main__":
    #data = list_of_dates("01/01/2019","08/31/2021")
    #download_gpw1(data,"10")