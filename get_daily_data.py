import requests
import gpw
import stockDB_manager
import tools
# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


def main () -> None:

    gpw.clear_data()
    last_day = stockDB_manager.take_last_date('stock.stg_gpw')
    today = tools.current_date()
    list_to_download = tools.list_of_dates(last_day,today) #change to tools.list_of_dates
    instruments_to_download = ["1","10"]
    #gpw.check_conection if true downlad if not
    #gpw.get_downloaded_dates()
    gpw.gpw_download(list_to_download,instruments_to_download)
    gpw.merge_data()
    pass




if __name__ == "__main__":
    main()
    