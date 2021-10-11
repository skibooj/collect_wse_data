import requests
import gpw


# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


def main () -> None:

    
    instruments_to_download = ["1","10"]
    date_range = gpw.list_of_dates(period_start='01/01/2010',period_end='01/09/2021')
    gpw.download_gpw(date_range,instruments_to_download)
    for element in instruments_to_download:
        gpw.merge_data(element)
    
    pass




if __name__ == "__main__":
    main()

    