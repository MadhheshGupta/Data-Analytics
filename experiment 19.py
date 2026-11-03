print("Name :", "Madhesh Gupta ,", "Enrollment_No. :", "0863CS231095")

import pandas as pd

data = {
    "Name":
        ["Aarav", "Bhavna", "Chirag", "Disha", "Eshan",
         "Fatima", "Gaurav", "Heena", "Ishaan", "Jaya"],

    "Age":
        [21, 22, 20, 23, 21, None, 24, 20, 23, 21],

    "Department":
        ["CSE", "AI&DS", "CSE", "ECE", "MECH",
         "CSE", "AI&DS", "ECE", "CSE", "MECH"],

    "Marks":
        [88, 91, 76, 85, 70, 93, 67, 89, 74, 95],

    "City":
        ["Indore", "Bhopal", None, "Indore", "Jabalpur",
         "Indore", "Bhopal", "Ujjain", "Jabalpur", "Indore"]
}

df = pd.DataFrame(data)

pd.set_option('display.max_columns', None)
#~# create a object say pivot
pivot = pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    aggfunc=["sum", "mean", "median"]
)

print(pivot)
