print("Name :", "Madhesh Gupta,", "Enrollment_No. :", "0863CS231095")

import pandas as pd

data = {
    "Name": ["Arav", "Bhavna", "Chirag", "Disha", "Eshan",
             "Fatima", "Gaurav", "Heena", "Ishaan", "Jaya"],
    
    "Age": [21, 22, 20, 23, 21, 22, 24, 20, 23, 21],
    
    "Department": ["CSE", "AI&DS", "CSE", "ECE", "MECH",
                   "CSE", "AI&DS", "ECE", "CSE", "MECH"],
    
    "Marks": [88, 91, 76, 85, 70, 93, 67, 89, 74, 95],
    
    "City": ["Indore", "Bhopal", "Ujjain", "Indore", "Jabalpur",
             "Indore", "Bhopal", "Ujjain", "Jabalpur", "Indore"]
}

df = pd.DataFrame(data)

pd.set_option("display.max_columns", None)  # to display all columns
print(df)

print()

# Access single column
# syntax: df["column_name"]
print(df["Age"])

print()

# Access multiple columns
# syntax: df[["column1", "column2", ...]]
print(df[["Name", "Department"]])
