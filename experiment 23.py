print("Name :", "Madhesh Gupta ,", "Enrollment_No. :", "0863CS231095")


import pandas as pd

# create dataframe
data = {
    "Name": ["Nillakshi", "Harshali", "Sugandhi"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# write dataframe to CSV file
df.to_csv("student_data.csv", index=False)

print("CSV file created successfully")
