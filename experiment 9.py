print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

import pandas as pd

d1 = pd.DataFrame({
    'age1' : [20,30,40,50,None,60],
    'age2' : [10,20,30,None,18,20],
})

print(d1)

# adding new column
print()

d1["Sum"] = d1["age1"] + d1["age2"]
print(d1)

print()

d1["age1"] = d1["age1"] + 5
print(d1)

print()

# check who can vote
d1["check"] = d1["age1"] > 18
print(d1)

print(d1["check"].value_counts())
