import os
from pathlib import Path
import requests
import pandas as pd
from datetime import date, datetime
from pandas.core.indexes.datetimes import date_range
import glob



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


def gpw_download(
    dates_list: list=None,
    financial_instument: list=None):

    for each_instrument in financial_instument:
        
        source_path = Path.cwd()
        download_path = 'D_data'
        final_directory = Path(source_path,download_path,each_instrument)
        
        if not os.path.exists(final_directory):
            os.mkdir(final_directory)

        for each_date in dates_list:
            url = f"https://www.gpw.pl/archiwum-notowan?fetch=1&type={each_instrument}&instrument=&date={each_date}"
            print(url)
            resp = requests.get(url, verify=False)
            file_name = Path(final_directory,str(each_date + '.xls')
            with file_name.open(mode ='wb') as output:
                output.write(resp.content)
    pass


def merge_data(kind_of_element: str= None): #financial_instrument 
    files_list = glob.glob(f"./D_data/{kind_of_element}/*") #change to pathlib
    final_data = pd.DataFrame()
    error_list = []
    current_date = pd.to_datetime("today").strftime("%d-%m-%Y")


    for file in files_list:
        if file.endswith('.xls'):
            try:
                final_data = final_data.append(pd.read_excel(file), ignore_index=True)
            except ValueError:
                print(f"{file} --- Error: there was an error")
                error_list.append(file)
    
    # add time to name of file 
    pd.DataFrame(error_list).to_excel(f"{current_date}_error_logs_{kind_of_element}.xlsx")
    final_data.to_csv(f"{current_date}_final_date_{kind_of_element}.csv")
    
    pass 


def import_data(
    file_name: str =None,
    financial_instrument: str =None
) -> None:
    pass

def clear_data() -> None:                 
    pass 
                             
                                                  
if __name__ == "__main__":
    #test
    dates = list_of_dates('01/01/2021','10/01/2021')
    ins_to_download = ['1','10','13']
    gpw_download(dates,ins_to_download)
    for x in ins_to_download:
        merge_data(x)
