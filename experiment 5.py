print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

# head ---> to check the data type (top)
# tail ---> to check recent entries (bottom)
# syntax object.head(n) for n rows
# syntax object.tail(n) for n rows

import pandas as pd

d1 = [10,20,30,40,50,60,70,80,90,100,110,120,130]

s1 = pd.Series(d1)
print(s1)

print('top n data --->')
print(s1.head(3))

print('bottom n data --->')
print(s1.tail(3))

# order the values 
s2 = s1.sort_values(ascending=False)
print(s2)
