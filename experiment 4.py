print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

import pandas as pd

d1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}

s1 = pd.Series(d1, dtype=object)
print(s1)

# update a value of c = 'hello'

s1['c'] = 'hello'
print(s1)