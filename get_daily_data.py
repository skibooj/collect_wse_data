import requests
import gpw
import sql_manager

# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


def main () -> None:

    
    last_day = sql_manager.take_last_date_gpw("gpw_facts")
    instruments_to_download = ["1","10"]
    # gpw.download_gpw(last_day,instruments_to_download)
    # for element in instruments_to_download:
    #     gpw.merge_data(element)
    # gpw.gpw_data_preparation()
    
    pass




if __name__ == "__main__":
    main()
    