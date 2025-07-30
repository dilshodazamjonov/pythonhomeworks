import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2, 3],[2, 3, 4],[2, 4, 7]], columns=["A", "B", "C"])

print(df.head)

# For reading csv file 

# pd.read_csv('Filename')

# For reading json files

# df_json = pd.read_json('Filename')
# df_json.head('Value') # can give values like integer. By default it is 5


# FOR READING EXCEL SHEETS

# df_sheets = pd.read_excel('data/titanic.xlsx')

# print(df_sheets.head(10))

arr = np.arange(10)
view = arr[2:5]
view[:] = 99
print(arr)
