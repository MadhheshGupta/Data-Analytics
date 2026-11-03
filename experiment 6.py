print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

import pandas as pd

d1 = [10,20,30,40,50,60,70,None,80,90,100,110,120,130]

s1 = pd.Series(d1)
print(s1)

print() 

print("datatype : ", s1.dtype)
print("row no : ", s1.shape)
print("dimension 1/2/3 : ", s1.ndim)
print("size/len/total element: ", s1.size)
print("has none values : ", s1.hasnans)
print("is empty : ", s1.empty)
