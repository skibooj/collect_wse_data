import pandas as pd
import requests


# settings that skip warnings
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'



def list_of_dates(period_start=None,period_end=None) -> list:
    range_of_dates=pd.date_range(start=period_start,end=period_end,freq="B") 
    dates_to_download = range_of_dates.strftime("%Y-%m-%d").tolist() 
    return dates_to_download




def download_gpw(dates_list=None,
    financial_instument=None,
    file_destination=None
):
    """
    start - period start 
    end -   period end
    fin_in - which financial instrument do you want to download
    dest - where save final 
    """
    # dodac sciezke tak zeby dzialala na wielu platformach win/linux/macos
    # 
    for each_dates in dates_list:
        type_to_download = financial_instument
        url = f"https://www.gpw.pl/archiwum-notowan?fetch=1&type={type_to_download}&instrument=&date={each_dates}"
        resp = requests.get(url, verify=False)
        file_name = each_dates

        with open(f'/home/skibooj/work/gpw/{file_destination}/{type_to_download}/{file_name}.xls', 'wb') as output:
                output.write(resp.content) 

    pass
 



# merge data function
def merge_output_file(final_name='',
                          directory=''):
        """
        
        """
        pass

def merge_gpw_data(
    financial_instrument=None,
    final_directory=None):
    pass

def import_data_gpw():
    pass


if __name__ == "__main__":
    pass
    
    #data = list_of_date(period_start="07/01/2021",period_end="07/10/2021")
    #download_gpw(data,"10","D_data")