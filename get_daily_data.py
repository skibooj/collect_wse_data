from datetime import date
from pathlib import Path
import requests
import gpw
import stockDB_manager
import tools
import sys
import os
import pandas as pd
from datetime import datetime


# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'



def main () -> None:
    
    stock_name = 'GPW'
    dowloaded_files_path = Path('./D_data/')
    archive_file_name = Path('./archived_files/')
    merged_files_path = Path('./merged_files/')
    ready_files_path = Path('./ready_to_import/')
    security_type = ["1","10"] #1- indexes 10 - stocks
    imported_data = []
    
    last_date_in_db = stockDB_manager.take_last_date('GPW')
    today_date = tools.current_date()
    dates_rage = tools.list_of_dates(last_date_in_db,today_date)
    holidays = stockDB_manager.get_holidays(stock_name)
    dates_to_download = [day for day in dates_rage if day not in holidays]
    
    #TODO: archive data
    for folders in dowloaded_files_path.glob('*'):
        tools.remove_files(folders)
    tools.remove_files(merged_files_path)
    tools.remove_files(ready_files_path)


    if len(dates_to_download) == 0:
        print('there is nothing to download')
        sys.exit()
    else:
        print(f"{len(dates_to_download)} files will be downloaded")
    
    
    dates_to_download = [day.strftime('%d-%m-%Y') for day in dates_to_download]
    del dates_to_download[0] #to avoid duplicate last date in database
    
    #TODO: compare already dowload files with files to dowload to avoid unecessery dowloading
    
    if_data_dowloaded = False
    try:
        #gpw.gpw_download(dates_to_download,security_type)
        if_data_dowloaded = True
    except:
        print('there is a problem with dowloading')


    dowloanded_folders = tools.get_list_of_folders(dowloaded_files_path)
    for folder in dowloanded_folders:
        gpw.merge_data(folder)
    
    
    merged_files = tools.get_list_of_file(merged_files_path)

    if len(merged_files) == 0:
        print('there is nothing to merge')
        sys.exit()
    else:
        pass
    
 
    for file in merged_files:
        security_type = file.parts[1]
        print(file)
        gpw.import_preparation(file_dir=file,security_type=security_type,final_directory=ready_files_path)
 

    # ready_files = tools.get_list_of_file(ready_files_path)  
    # stockDB_manager.clear_table(table_name="stg_gpw")
    # for file in ready_files:
    #    stockDB_manager.bulk_insert(file_path=file.absolute(),table_name='stg_gpw')
    # # stockDB_manager.refresh_dim(stock_name='GPW')
    # stockDB_manager.load_to_main_table(staging_table="stg_gpw")
    # # stockDB_manager.refresh_data_marts()
    # # if_data_dowloaded = False


if __name__ == "__main__":
    #ready_files_path = Path('./ready_to_import/')
    #tools.remove_files(ready_files_path)
    main()
    
