print("Name :", "Madhesh Gupta ,", "Enrollment_No. :", "0863CS231095")

import pandas as pd
import numpy as np

def grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 60:
        return "C"
    else:
        return "D"

df = pd.DataFrame({
    "Name": ["ID_" + str(i) for i in range(1000)],
    "Maths": np.random.randint(40, 100, 1000),
    "Science": np.random.randint(40, 100, 1000),
    "English": np.random.randint(40, 100, 1000),
    "Attendance": np.random.randint(60, 100, 1000)
})

print(df)
#~? find Total and create a new column
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
#~? same for percentage
df["Percentage"] = df["Total"] / 3

#~# grading
df["Grade"] = df["Percentage"].apply(grade)
print()

pd.set_option('display.max_columns', None)
print(df)
