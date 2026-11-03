print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

# slice a series using position, index and labels
# syntax object[start : stop : step]
# here start can be index and default it start from position

# position   index   Value 
#    0        jan     31
#    1        feb     28
#    2        mar     31

import pandas as pd

d1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}

s1 = pd.Series(d1)
print(s1)

print(s1['a':'c']) # argument passes here is index
print(s1[2:5])     # argument passed here is position
