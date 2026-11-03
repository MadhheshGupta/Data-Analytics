print("Name :", "Madhesh Gupta ,", "Enrollment_No. :", "0863CS231095")

import pandas as pd

# read CSV file and convert into dataframe
df = pd.read_csv("student_data.csv")

# display dataframe
print("DataFrame:")
print(df)

print("\n------------------")

# basic analysis
print("Shape of DataFrame:", df.shape)
print("Columns:", df.columns.tolist())

print("\nStatistical Summary:")
print(df.describe())

print("\nMaximum Marks:")
print(df["Marks"].max())

print("\nMinimum Marks:")
print(df["Marks"].min())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nStudent with Highest Marks:")
print(df[df["Marks"] == df["Marks"].max()])
