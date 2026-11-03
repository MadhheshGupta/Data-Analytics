print("Name :", "Madhesh Gupta ,", "Enrollment_No. :", "0863CS231095")

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['id' + str(i) for i in range(1000)],
    'maths': np.random.randint(60, 100, 1000),
    'science': np.random.randint(60, 100, 1000),
    'english': np.random.randint(60, 100, 1000),
    'attendance': np.random.randint(30, 100, 1000),
})

print(df)
print('--' * 20)

#~# sorting marks
sorted_df = df.sort_values(by="maths")
print(sorted_df)

print('--' * 20)

#~# sort marks by descending order
sort_df = df.sort_values(by="maths", ascending=False)
print(sort_df)

#~# sort multiple columns
print('--' * 20)

sorted_df = df.sort_values(
    by=["maths", "science"],
    ascending=[False, True]
)

print(sorted_df)
