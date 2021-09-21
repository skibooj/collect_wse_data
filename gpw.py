import os
from pathlib import Path
from pandas.core.frame import DataFrame
import requests
import pandas as pd
from datetime import datetime
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
          
            base_url ='https://www.gpw.pl/archiwum-notowan'
            url_params = {'fetch':'1',
                      'type':each_instrument,
                      'date':each_date}
            
            resp = requests.get(base_url, params=url_params, verify=False)
            file_name = Path(final_directory, str(each_date + '.xls'))

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
    
    #change to path and change to txt
    pd.DataFrame(error_list).to_csv(f"./error_logs/{current_date}_error_logs_{kind_of_element}.csv")
    final_data.to_csv(f"./merged_files/{current_date}_merged_data_{kind_of_element}.csv", index= False)
    
    pass 


def detele_data(file_name: str=None) -> None:
    if file_name == None:
        file_name = "D_data"
    
    pass                                         

def gpw_data_preparation(file_name: str, final_directory: str=None) -> None:
 
    if final_directory ==None:
        final_directory="./"

    data = pd.read_csv(file_name)
    data = data.rename(columns={'Data':'date',
                            'Nazwa':'symbol',
                            'Waluta':'currency',
                            'Kurs otwarcia':'open',
                            'Kurs max':'max',
                            'Kurs min':'min',
                            'Kurs zamknięcia':'close',
                            'Zmiana':'%change',
                            'Wolumen':'quantity',
                            'Liczba Transakcji':'number of transactions',
                            'Obrót':'volume',
                            'Liczba otwartych pozycji':'number of open positions',
                            'Wartość otwartych pozycji':'value of open positions',
                            'Cena nominalna': 'nominal price',
                           })
    data['volume'] = data['volume'].apply(lambda x: x*1000)
    data['date']= pd.to_datetime(data['date'])
    
    
    final_name = Path(file_name).stem + '_ready_to_import.csv'
    path_to_save = Path(final_directory,Path(file_name).stem + '_ready_to_import.csv')
    data.to_csv(path_to_save,index=False)
    pass


if __name__ == "__main__":
    #test
    #dates = list_of_dates('01/01/2019','07/09/2021')
    instruments_to_download = ['10']
    #gpw_download(dates,instruments_to_download)
    for element in instruments_to_download:
        merge_data(element)



