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
    merged_files_path = './merged_file/'
    ready_files_path = ''   #complete
    stock_name = 'GPW'
    financial_instruments = ["1","10"]
    
    
    last_day = stockDB_manager.take_last_date('stock.stg_gpw')
    today = tools.current_date()
    dates_rage = tools.list_of_dates(last_day,today)
    holidays = stockDB_manager.get_holidays(stock_name)
    dates_to_dowload = set(dates_rage).difference(holidays)
    
    
    
    #gpw.clear_data()
    #gpw.move_to_archive()
    
    if len(dates_to_dowlonad) == 0:
        print('there is nothing to download')
        sys.exit()
    else:
        pass
    
    # for each retrieved item, check whether it contains data
    # if file contain error delete it
    # like above check if the folder contain any files
    # use try except statement
    
    
    #if gpw.check_dowloaded_file(file_path=dowloaded_files_path) == True:
        #pass
    #else:
        #print('dowloaded data has error')
        #sys.exit()
       

    
    gpw.gpw_download(list_to_download,financial_instruments)
    gpw.merge_data()
    
    #gpw.check_merged_data()
    
    #stockDB_manager.bulk_insert(file_path=ready_files_path,stock_name='GPW')
    #sotckDB_manage.refresh_dim()
    #stockDB_manager.load_to_main_table()
    
    pass


if __name__ == "__main__":
    main()
    
