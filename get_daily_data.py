import requests
import gpw
import stockDB_manager
import tools

# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


def main () -> None:
    stock_name = 'GPW'
    dowloaded_files_path = './dowloaded_data/'
    archived_files_path = './archived_file/'
    merged_files_path = './merged_file/'
    ready_files_path = ''   #complete
    stock_name = 'GPW'
    financial_instruments = ["1","10"]
    
    
    last_day = stockDB_manager.take_last_date('stock.stg_gpw')
    today = tools.current_date()
    dates_rage = tools.list_of_dates(last_day,today)
    holidays = stockDB_manager.get_holidays(stock_name)
    dates_to_dowload = set(dates_rage).difference(holidays)
    
    
    tools.move_to_archive(output_file=archived_files_path,dir_name=dowloaded_files_path)
    tools.remove_file(folder_dir=dowloaded_files_path)
    
    
    if len(dates_to_dowlonad) == 0:
        print('there is nothing to download')
        sys.exit()
    else:
        pass
   
      
    gpw.gpw_download(list_to_download,financial_instruments)
    gpw.merge_data()
    

    stockDB_manager.bulk_insert(file_path=ready_files_path,stock_name='GPW')
    #sotckDB_manage.refresh_dim()
    #stockDB_manager.load_to_main_table()
    
    pass


if __name__ == "__main__":
    main()
    
