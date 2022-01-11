import os
from pathlib import Path
from pandas.core import tools
from pandas.core.frame import DataFrame
import requests
import pandas as pd
from datetime import datetime
from pandas.core.indexes.datetimes import date_range
import glob
import tools

# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


def gpw_download(dates_list:list,financial_instument:list) -> None:

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
            file_dir = Path(final_directory, str(each_date + '.xls'))

            with file_dir.open(mode ='wb') as output:
                output.write(resp.content)                         
    pass


def merge_data(folder_dir:Path) -> bool:

    final_data = pd.DataFrame()
    error_list = []
    current_date = tools.current_date("%Y-%m-%d")
    files_list = folder_dir.glob('*.xls')
    for file in files_list:
        try:
            final_data = final_data.append(pd.read_excel(file), ignore_index=True)
        except ValueError:
            error_list.append(file)
    print(f"success with {final_data.shape[0]} file(s) in {folder_dir}")
    print(f"errors with {pd.DataFrame(error_list).shape[0]} file(s) in {folder_dir}")
    
    error_file_name = f"{current_date}_error_logs_{folder_dir.stem}.csv" 
    merged_file_name = f"{current_date}_merged_data_{folder_dir.stem}.csv"
    error_file_dir = Path('./error_logs/',error_file_name)
    merged_file_dir = Path('./merged_files/',merged_file_name) 
    
    if len(final_data) == 0:
        print ("nothing to merge, check dowloanded files")
        return False 
    else:
        pd.DataFrame(error_list).to_csv(error_file_dir)
        final_data.to_csv(merged_file_dir, index= False) 
    
    return True
                                        

# test this function
def import_preparation(file_dir: str, security_type:str, final_directory: str=None) -> None:
    
    if final_directory ==None:
        final_directory=Path('./ready_to_import/')

    data = pd.read_csv(file_dir)
    
    data = data.rename(columns={'Data':'date',
                            'Nazwa':'symbol',
                            'Waluta':'currency',
                            'ISIN':'isin',
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
    data['stock_name'] = 'GPW'
    data['currency'] = 'PLN'
    data['country'] = 'Poland'  
    data['date']= pd.to_datetime(data['date'])
    data['volume'] = data['volume'].apply(lambda x: x*1000)
    data['security_type'] = security_type

    data = data.loc[:, ['date','stock_name','country','currency','security_type','symbol','isin','open',
                        'max','min','close','%change','quantity',
                        'number of transactions','volume','number of open positions',
                        'value of open positions','nominal price',]]
    
    path_to_save = Path(final_directory,Path(file_dir).stem + '_ready_to_import.csv')
    data.to_csv(path_to_save,index=False)
    pass


if __name__ == "__main__":
    pass