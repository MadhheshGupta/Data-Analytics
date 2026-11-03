print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")
import pandas as pd

d1 = {
    "name" : ["a", "b", "c", "d", "e"],
    "dept" : ["sales", "office", "IT", "marketing", "accountant"],
    "salary" : [1000,2000,3000,1500,2000],
    "city" : ['i', 'd', None, 'm', 'k'],
    "gender" : ['m', 'm', 'f', 'm', 'f']
}
df = pd.DataFrame(d1)
print(df)
print()
# to see all column data
pd.set_option('display.max_columns', None)
print(df)

# create a dataframe with list 
name = ["a", "b", "c", "d", "e"]
dept = ["sales", "office", "IT", "marketing", "accountant"]
salary = [1000,2000,3000,1500,2000]
city = ['i', 'd', None, 'm', 'k']
gender = ['m', 'm', 'f', 'm', 'f']

print()

df = pd.DataFrame({
    'name' : name,
    'dept' : dept,
    'salary' : salary,
    'city' : city,
    'gender' : gender
})
print(df)
