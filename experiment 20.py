print("Name :", "Madhesh Gupta ,", "Enrollment_No. :", "0863CS231095")

import pandas as pd

# Creating dictionary data
data = {
    "Name": ["Aarav", "Bhavna", "Chirag", "Disha", "Eshan",
             "Fatima", "Gaurav", "Heena", "Ishaan", "Jaya"],

    "Department": ["CSE", "AI&DS", "CSE", "ECE", "MECH",
                   "CSE", "AI&DS", "ECE", "CSE", "MECH"],

    "City": ["Indore", "Bhopal", "Indore", "Indore", "Jabalpur",
             "Indore", "Bhopal", "Ujjain", "Jabalpur", "Indore"],

    "Marks": [88, 91, 76, 85, 70, 93, 67, 89, 74, 95]
}
# Create DataFrame
df = pd.DataFrame(data)

# Display all columns
pd.set_option('display.max_columns', None)

print("Original DataFrame")
print(df)
print("\n", "--" * 20)

# Creating Pivot Table
pivot = pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    columns="City",
    aggfunc="mean"
)
print("Pivot Table")
print(pivot)
