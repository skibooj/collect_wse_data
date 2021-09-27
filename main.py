import requests
import gpw


# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


def main () -> None:

    #demo
    start_date = "01/01/2015"
    end_date =  "20/01/2021"
    financial_instrument = "10" #stock 
    data = gpw.list_of_dates(start_date,end_date)
    gpw.download_gpw(data,financial_instrument)
    gpw.merge_data(financial_instrument)
    pass


if __name__ == "__main__":
    main()
    