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

## mean --> Average
print('mean -->')
print(df.mean(numeric_only=True))

## specific column
# df['column'].mean()

## median --> middle value
print('median -->')
print(df.median(numeric_only=True))

## mode --> most frequent value
print('mode -->')
print(df.mode(numeric_only=True))
