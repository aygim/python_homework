import pandas as pd

df = pd.read_csv("../csv/employees.csv")

employee_names = [row['first_name'] + " " + row['last_name'] for index, row in df.iterrows()]
print(employee_names)

employee_names_with_e = [name for name in employee_names if 'e' in name]
print("Employee names with e:")
print(employee_names_with_e)

