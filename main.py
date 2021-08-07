import requests
from . import gpw


# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


def main () -> None:

    start_date = "01/08/2021"
    end_date =  "31/08/2021"

    data = gpw.list_of_dates(start_date,end_date)
    gpw.download_gpw1(data)
    gpw.merge_data("10")
    pass


if __name__== "__main__.py":
    main()
    