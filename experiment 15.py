print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

import pandas as pd
import numpy as np

data = {
    'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Age': [21, 22, 20, 23, 24, 22, 21, 23, 22, 24],
    'Marks': [85, 90, 78, 88, 92, 76, 84, 89, 91, 87],
    'Salary': [30000, 32000, 28000, 35000, 37000, 29000, 31000, 36000, 34000, 33000],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance']
}

df = pd.DataFrame(data)

pd.set_option('display.max_columns', None)
print(df)

# min
print(df.min())    # min value from each column 
print(df.max())    # max value from each column

# max and min from specific columns 
# df[["column name"]].min()

print()
print(df[['Salary', 'Age']].min())

# specific row syntax --> df.iloc[start:stop].min
print('row -->')
print(df.iloc[3:6].min(numeric_only=True))
