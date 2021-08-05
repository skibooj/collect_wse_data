import os
import requests
import urllib3
import pandas as pd
from datetime import date, datetime
from pandas.core.indexes.datetimes import date_range


# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'

# create range of date in certain format
range_of_date=pd.date_range(start="07/01/2021",end="7/31/2021",freq="B") 
dates_to_download = range_of_date.strftime("%Y-%m-%d").tolist()

# type to download
# 1 - index
# 10 - stock shares
# 13 - treasury bonds
# 17 - pre-emptive rights (?)
# 35 - futures contracts
# 37 - rights to shares (?)
# 48 - investment certificates
# 53 - warannts
# 54 - Index unit
# 66 - options
# 161 - structured products
# 241 - ETF
# 301 - IPO
# ks - shorts
# konktrakt_okr - final settlement price
# opcje_kr - (?)
# pack_quote - (?)
# pack_biso - (?)



#create directory if not exist

for each_dates in dates_to_download:
    type_to_download = "10"
    url = f"https://www.gpw.pl/archiwum-notowan?fetch=1&type={type_to_download}&instrument=&date={each_dates}"
    resp = requests.get(url, verify=False)
    file_name = each_dates
    with open(f'/home/skibooj/work/gpw/D_data/{type_to_download}/{file_name}.xls', 'wb') as output:
            output.write(resp.content)




#if __name__ == "__main__":
#    pass
    
