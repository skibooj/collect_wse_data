import pandas as pd
from datetime import datetime
import shutil
from pathlib import Path
import zipfile
import glob 
import os
import shutil


def get_list_of_file(dir_name:Path) -> list:
    list_of_file = list(Path(dir_name).rglob( '*.*' ))
    return list_of_file

def get_list_of_folders(dir_name:Path) -> list:
    list_of_folders = list(dir_name.glob('./*'))
    return list_of_folders

def current_date(format=None)-> str:
    if format == None:
        format = "%d/%m/%Y"
    today = pd.to_datetime("today").strftime(format)
    return today


def list_of_dates(period_start: str = None,period_end: str = None) -> list:
    """
    data shoud have format: dd/mm/yyyy
    """
    
    ps = datetime.strptime(period_start, "%d/%m/%Y").strftime("%m-%d-%Y")
    pe = datetime.strptime(period_end, "%d/%m/%Y").strftime("%m-%d-%Y")
    
    # freq argument is a constant because stock exchange work only in a workdays
    range_of_dates=pd.date_range(start=ps,end=pe,freq="B")
    range_of_dates=list(pd.to_datetime(range_of_dates))
    return range_of_dates


def remove_files(folder_dir:Path):
    files = glob.glob(f"{folder_dir}/*")
    for f in files:
        os.remove(f)
    pass

if __name__ == "__main__":
    pass
