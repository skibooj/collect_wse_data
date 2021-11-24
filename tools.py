import pandas as pd
from datetime import datetime
import shutil
from pathlib import Path
import zipfile
import glob 
import os
import shutil


def get_list_of_file(dir_name:Path) -> list:
    list_of_file = list(Path(dir_name).rglob( '*' ))
    return list_of_file


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



def remove_file(folder_dir:Path):
    path_to_check = Path(f'./{folder_dir}/')
    list_of_folders = [x for x in path_to_check.iterdir() if x.is_dir()]
    for folder in list_of_folders:   
        files = folder.glob('*')
        for f in files:
            os.remove(f)
        pass


if __name__ == "__main__":
    dowloaded_files_path = Path('./D_data/')
    archived_files_path = Path('/archived_file/archive.zip')
    #archive_dowloaded_data(source=dowloaded_files_path,destination=archived_files_path)
    print(get_list_of_file(dowloaded_files_path))
    pass
