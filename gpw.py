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


def merge_data(folder_dir:str) -> None:
    
    if folder_dir == None:
        folder_dir = Path('D_data')

    path_to_check = Path(f'./{folder_dir}/')
    list_of_folders = [x for x in path_to_check.iterdir() if x.is_dir()]
    
    final_data = pd.DataFrame()
    error_list = []
    current_date = pd.to_datetime("today").strftime("%Y-%m-%d")

    for security_type in list_of_folders:

        files_list = security_type.glob('*.xls')

        for file in files_list:
            try:
                final_data = final_data.append(pd.read_excel(file), ignore_index=True)
            except ValueError:
                print(f"{file} --- Error: there was an error")
                error_list.append(file)
        
        #>>security_type
        # .parts[1] output: instrument number
        error_file_name = f"{current_date}_error_logs_{security_type.parts[1]}.csv" 
        merged_file_name = f"{current_date}_merged_data_{security_type.parts[1]}.csv"
        
        error_file_dir = Path('./error_logs/',error_file_name)
        merged_file_dir = Path('./merged_files/',security_type.parts[1],merged_file_name)
        

        if not os.path.exists(Path(f'./merged_files/{security_type.parts[1]}')):
            os.mkdir(Path(f'./merged_files/{security_type.parts[1]}'))
        
            
        pd.DataFrame(error_list).to_csv(error_file_dir)
        final_data.to_csv(merged_file_dir, index= False)
        
    pass 
                                        

# test this function
def import_preparation(file_dir: str, security_type
:str, final_directory: str=None) -> None:
    
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