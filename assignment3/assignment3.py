import pandas as pd
# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# 1.1
myDict = {  'Name': ['Alice', 'Bob', 'Charlie'], 
                'Age': [25, 30, 35], 
                'City': ['New York', 'Los Angeles', 'Chicago']}
task1_data_frame = pd.DataFrame(myDict)
print(task1_data_frame)

# 1.2
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

# 1.3
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print(task1_older)

# 1.4
task1_older.to_csv('employees.csv', index = False)

# Task 2: Loading Data from CSV and JSON

# 2.1
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)
print(task2_employees.columns)
print(task2_employees.info())

# 2.2
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

# 2.3.
more_employees = pd.concat([task2_employees,json_employees],ignore_index=True)
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods

# 3.1
first_three = more_employees.head(3)
print(first_three)
# 3.2
last_two = more_employees.tail(2)
print(last_two)
# 3.3
employee_shape = more_employees.shape
print(employee_shape)
# 3.4
print(more_employees.info())

# Task 4: Data Cleaning
# 4.1
dirty_data = pd.read_csv("dirty_data.csv")
clean_data = dirty_data.copy()
print(clean_data)

# 4.2
clean_data.drop_duplicates(inplace=True)
print(clean_data)

# 4.3
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
clean_data["Age"].fillna(clean_data["Age"].mean(), inplace=True)
print(clean_data)

# 4.4
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print(clean_data)

# 4.5
clean_data["Age"].fillna(clean_data["Age"].mean(), inplace=True)
clean_data["Salary"].fillna(clean_data["Salary"].median(), inplace=True)
print(clean_data)

# 4.6
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print(clean_data)

# 4.7
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print(clean_data)