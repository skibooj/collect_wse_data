from datetime import date
from pathlib import Path
import requests
import gpw
import stockDB_manager
import tools
import sys
import os
    
# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
import shutil

def main () -> None:
    stock_name = 'GPW'
    dowloaded_files_path = Path('./D_data/')
    archive_file_name = Path('./archived_file/')
    merged_files_path = Path('./merged_file/')
    ready_files_path = ''   #complete
    stock_name = 'GPW'
    financial_instruments = ["1","10"] #1- index 10 - stock
    
    
    last_day = stockDB_manager.take_last_date('stg_gpw')
    today = tools.current_date()
    dates_rage = tools.list_of_dates(last_day,today)
    holidays = stockDB_manager.get_holidays(stock_name)
    dates_to_download = [day for day in dates_rage if day not in holidays]
    

    #achive and then delete dowloaded files
    number_of_files = sum([len(files) for r, d, files in os.walk(dowloaded_files_path)])
    if number_of_files == 0:
        print('no files to archive')
    else:
        output_filename=Path(archive_file_name,str(f"arch_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}"))
        shutil.make_archive(output_filename, 'zip', dowloaded_files_path)
    tools.remove_file(folder_dir=dowloaded_files_path)

        
    if len(dates_to_download) == 0:
        print('there is nothing to download')
        sys.exit()
    else:
        print(f"{len(dates_to_download)} files will be downloaded")
   

    dates_to_download = [day.strftime('%m-%d-%Y')for day in dates_to_download]
    gpw.gpw_download(dates_to_download,financial_instruments)
    # gpw.merge_data()
    

    # stockDB_manager.bulk_insert(file_path=ready_files_path,stock_name='GPW')
    # sotckDB_manage.refresh_dim()
    # stockDB_manager.load_to_main_table()
    
    pass


if __name__ == "__main__":
    main()
    
