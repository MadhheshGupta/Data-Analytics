print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

# basic operations on series
# same index ---> operation will happen
# for different index it will return NaN

import pandas as pd

d1 = [10,20,30,40,50,60]
d2 = {'jan':31, 'feb':28, 'march':31, 'april':30, 'may':31, 'june':30}
d3 = [20,40,50,60]

s1 = pd.Series(d1)
s2 = pd.Series(d2)
s3 = pd.Series(d3)

s4 = s1 + s2    # addition on series
print("s4 --->")
print(s4)

s5 = s1 - s3   # subtraction on series
print("s5 --->")
print(s5)