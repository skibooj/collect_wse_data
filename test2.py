import pandas as pd
import requests

def list_of_date(period_start=None,period_end=None) -> list:
    range_of_date=pd.date_range(start=period_start,end=period_end,freq="B") 
    dates_to_download = range_of_date.strftime("%Y-%m-%d").tolist() 
    return dates_to_download


def download_gpw(dates_list=None,
    financial_instument=None,
    dest=None
):
    """
    start - period start 
    end -   period end
    fin_in - which financial instrument do you want to download
    dest - where save final 
    
    
    """
    for each_dates in dates_list:
        type_to_download = financial_instument
        url = f"https://www.gpw.pl/archiwum-notowan?fetch=1&type={type_to_download}&instrument=&date={each_dates}"
        resp = requests.get(url, verify=False)
        file_name = each_dates
        # add 
        with open(f'/home/skibooj/work/gpw/{dest}/{type_to_download}/{file_name}.xls', 'wb') as output:
                output.write(resp.content) 

    return True
 


if __name__ == "__main__":
    data = list_of_date(period_start="07/01/2021",period_end="07/10/2021")
    download_gpw(data,"10","D_data")
    