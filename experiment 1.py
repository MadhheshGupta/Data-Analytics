print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

# PANDAS : 
# pan = panel
# das = data structure
# 1d = series data structure
# 2d = dataframe, tabular format
# 3d = panel data structure

import pandas as pd

d1 = [31,28,None,30,31]  # NaN = Not a Number
index = ["jan", "feb", "mar", "april", "may"]

s1 = pd.Series(d1,index)
print(s1)

# to print specific value
print(s1['feb'])

# to update value
s1['feb'] = 29
print(s1)

d2 = {
    "fruit" : "apple",
    "climate" : "cold",
    "price" : 120
}

s2 = pd.Series(d2)
print(s2)

# to know basic details of series
print()
print("s1 datatype : ", s1.dtype)
print("rows : ", s1.shape)
print("dimension : ", s1.ndim)
print("size/len : ", s1.size)
print("none value : ", s1.hasnans)
print("empty : ", s1.empty)