import os
import requests
import urllib3
import time
import pandas as pd
from datetime import date, datetime
from pandas.core.indexes.datetimes import date_range


# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


range_of_date=pd.date_range(start="07/01/2021",end="7/31/2021")
dates_to_download = range_of_date.strftime("%Y-%m-%d").tolist()


for each_dates in dates_to_download:
    type_to_download = "1"
    url = f"https://www.gpw.pl/archiwum-notowan?fetch=1&type={type_to_download}&instrument=&date={each_dates}"
    resp = requests.get(url, verify=False)
    file_name = each_dates
    with open(f'/home/skibooj/work/gpw/D_data/{type_to_download}/{file_name}.xls', 'wb') as output:
            output.write(resp.content)





# df = pd.DataFrame()
# for file in sheets:
#      if file.endswith('.xlsx'):
#          df = df.append(pd.read_excel(file), ignore_index=True) 
# df.head()