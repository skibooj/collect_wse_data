import pandas as pd
from datetime import datetime
import shutil
from pathlib import Path
import zipfile
import glob 
import os
import shutil


def current_date()-> str:
    today = pd.to_datetime("today").strftime("%d/%m/%Y")
    return today


def list_of_dates(period_start: str = None,period_end: str = None) -> list:
    """
    data shoud have format: dd/mm/yyyy
    """
    
    ps = datetime.strptime(period_start, "%d/%m/%Y").strftime("%m-%d-%Y")
    pe = datetime.strptime(period_end, "%d/%m/%Y").strftime("%m-%d-%Y")
    
    # freq argument is a constant because stock exchange work only in a workdays
    range_of_dates=pd.date_range(start=ps,end=pe,freq="B")
    range_of_dates=pd.to_datetime(range_of_dates)
    #dates_to_download = range_of_dates.strftime("%d-%m-%Y").tolist() 
    return list(range_of_dates)


   

def archive_dowloaded_data(folder_to_archive:str=None,final_dir:str=None) -> None:
    files_list = Path(folder_to_archive).glob('*')
    for folder in files_list:
        #print(folder.stem)
        shutil.make_archive(folder.stem, 'zip',folder,final_dir)


def make_archive(source: Path, destination: Path) -> None:
    base_name = destination.parent / destination.stem
    fmt = destination.suffix.replace(".", "")
    root_dir = source.parent
    base_dir = source.name
    shutil.make_archive(str(base_name), fmt, root_dir, base_dir)


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
    make_archive(dowloaded_files_path,archived_files_path)
    pass
