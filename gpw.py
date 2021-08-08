import os
import requests
import urllib3
import pandas as pd
from datetime import date, datetime
from pandas.core.indexes.datetimes import date_range
import glob

# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


def list_of_dates(period_start: str = None,period_end: str = None) -> list:
    
    """
    data shoud have format: dd/mm/yyyy
    """

    ps = datetime.strptime(period_start, "%d/%m/%Y").strftime("%m-%d-%Y")
    pe = datetime.strptime(period_end, "%d/%m/%Y").strftime("%m-%d-%Y")

    # frequency is a constant because stock exchange work only in a workdays
    range_of_dates=pd.date_range(start=ps,end=pe,freq="B")
    dates_to_download = range_of_dates.strftime("%d-%m-%Y").tolist() 
    return dates_to_download


# type to download
# 1 - index
# 10 - stock shares
# 13 - treasury bonds
# 17 - pre-emptive rights (?)
# 35 - futures contracts
# 37 - rights to shares (?)
# 48 - investment certificates
# 53 - warannts
# 54 - Index unit
# 66 - options
# 161 - structured products
# 241 - ETF
# 301 - IPO
# ks - shorts
# konktrakt_okr - final settlement price
# opcje_kr - (?)
# pack_quote - (?)
# pack_biso - (?)



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





def merge_data(financial_instrument: str= None):    
    kind_of_element = '10'
    #glob.glob("./D_data/{kind_of_element}/*")
    sheets = glob.glob(f"./D_data/{kind_of_element}/*")
    final_data = pd.DataFrame()
    error_list = []
    current_date = "today1_date" #add pandas fct

    for file in sheets:
        if file.endswith('.xls'):
            try:
                final_data = final_data.append(pd.read_excel(file), ignore_index=True)
            except ValueError:
                print(f"{file[11:]} --- Error: there was an error")
                error_list.append(file)
    
    pd.DataFrame(error_list).to_excel(f'{current_date}_error_logs.xlsx')
    final_data.to_excel(f'final_date_{kind_of_element}.xlsx')
    pass 



if __name__ == "__main__":
    data = list_of_dates("01/08/2021",'10/08/2021')
    print(data)
