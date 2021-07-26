import glob
import pandas as pd


# wylaczenie z tego wszystkiego niedziel


kind_of_element = '1'
#glob.glob("./D_data/{kind_of_element}/*")
sheets = glob.glob("./D_data/1/*")
counter = 1
df = pd.DataFrame()
for file in sheets:
    print(f"{counter} ---- {file} jest brany pod uwage")
    if file.endswith('.xls'):
        df = df.append(pd.read_excel(file), ignore_index=True)
        print(f"{counter} ---- {file} gotowy")
        counter += 1 






print(df.shape)



