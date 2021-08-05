import glob
import pandas as pd



kind_of_element = '1'
#glob.glob("./D_data/{kind_of_element}/*")
sheets = glob.glob("./D_data/1/*")
final_data = pd.DataFrame()
error_list = []
current_date = "today_date" #add pandas fct

for file in sheets:
    if file.endswith('.xls'):
        try:
            final_data = final_data.append(pd.read_excel(file), ignore_index=True)
        except ValueError:
            print(f"{file[11:]} --- Error: there was an error")
            error_list.append(file)
        




pd.DataFrame(error_list).to_excel(f'{current_date}_error_logs.xlsx')
final_data.to_excel('final_date{kind_of_element}.xlsx')



