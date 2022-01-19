from pathlib import Path
import requests
import gpw
import stockDB_manager
import tools
import sys

# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'

def main () -> None:
    
    stock_name = 'GPW'
    dowloaded_files_path = Path('./D_data/')
    merged_files_path = Path('./merged_files/')
    ready_files_path = Path('./ready_to_import/')
    security_type = ["1","10"] #1- indexes 10 - stocks
    
    last_date_in_db = stockDB_manager.take_last_date('GPW')
    today_date = tools.current_date()
    dates_rage = tools.list_of_dates(last_date_in_db,today_date)
    holidays = stockDB_manager.get_holidays(stock_name)
    dates_to_download = [day for day in dates_rage if day not in holidays]
    

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
    print(dates_to_download)

    try:
        gpw.gpw_download(dates_to_download,security_type)
    except:
        print('there is a problem with dowloading')
        sys.exit()


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
 

    stockDB_manager.clear_table(table_name="stg_gpw")
    ready_to_import_files = tools.get_list_of_file(ready_files_path)  
    for file in ready_to_import_files:
       stockDB_manager.bulk_insert(file_path=file.absolute(),table_name='stg_gpw')


    stockDB_manager.load_to_main_table(staging_table="stg_gpw")
    print('end of process')


if __name__ == "__main__":
    main()
    
