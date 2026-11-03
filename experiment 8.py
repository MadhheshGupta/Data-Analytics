print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

import pandas as pd

d1 = {
    "name" : ["a", "b", "c", "d", "e"],
    "dept" : ["sales", "office", "IT", "marketing", "accountant"],
    "salary" : [1000,2000,3000,1500,2000],
    "city" : ['i', 'd', None, 'm', 'k'],
    "gender" : ['m', 'm', 'f', 'm', 'f']
}

df = pd.DataFrame(d1)

# to see all column data
pd.set_option('display.max_columns', None)
print(df)

# index value update
# syntax = object.index = [value, value, ...]
# for n rows we can use for loop 

df.index = [f'E_ID{i+1}' for i in range(len(df))]
print(df)
