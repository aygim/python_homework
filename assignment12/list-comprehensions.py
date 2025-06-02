import pandas as pd

df = pd.read_csv("../csv/employees.csv")

names = [row['first_name'] + " " + row['last_name'] for index, row in df.iterrows()]
print(names)

names_with_e = [name for name in names if 'e' in name]
print(names_with_e)

