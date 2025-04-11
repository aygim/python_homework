# Task 2: Read a CSV File
import csv
from datetime import datetime

def read_employees ():
    dict_emp = {}
    row_list = []
    try:
        with open('../csv/employees.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            dict_emp["fields"] = next(reader)
            for row in reader:
                    row_list.append(row)
            dict_emp["rows"] = row_list
            return dict_emp
        
    except Exception as e:
        print (f"SyntaxError: invalid syntax")
        exit()
    return emptyDict

employees = read_employees()

print(employees)

# Task 3: Find the Column Index
def column_index(column_name):
        try:
            return employees["fields"].index(column_name)
            
        except ValueError as e:
            return None
        
employee_id_column = column_index("employee_id")
print(employee_id_column)


# Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_ind = column_index("first_name")
    row = employees['rows'][row_number]
    value = row[first_name_ind]
    return value
print(employees)


# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
            return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
     matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
     return matches
# result = employee_find_2(3)  
# print(result)

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
     last_name_ind = column_index("last_name")
    #  print("Before sorting:", employees["rows"])
     employees["rows"].sort(key = lambda x: x[last_name_ind])
    #  print("After sorting:", employees["rows"])
     return employees["rows"] 
sorted_rows = sort_by_last_name()
print(employees)


# Task 8: Create a dict for an Employee
def employee_dict(row):
     fields = employees["fields"][1:] 
     result_dict = dict(zip(fields, row[1:]))
     return result_dict
employee = employees["rows"][0]
result = employee_dict(employee)
print(result)


# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
     all_employees = {}
     for row in employees["rows"]:
        employee_id = row[0]
        employee_info = employee_dict(row)
        all_employees[employee_id] = employee_info
     return all_employees   
result = all_employees_dict()
print(result)    


# Task 10: Use the os Module
import os
def get_this_value():
     return os.getenv('THISVALUE')
print(get_this_value())


# Task 11: Creating Your Own Module
import custom_module
def set_that_secret(secret):
     custom_module.set_secret(secret)
set_that_secret("my_new_secret")
print (custom_module.secret)


# Task 12: Read minutes1.csv and minutes2.csv
import csv

def read_minutes():
    minutes1, minutes2= {}, {}
    row_list = []
    with open('../csv/minutes1.csv', 'r') as file:
        minutes_1 = csv.reader(file)
        minutes1["fields"] = next(minutes_1)
        for row in minutes_1:
            row_list.append(tuple(row))
        minutes1["rows"] = row_list
           
    row_list = []
    with open('../csv/minutes2.csv', 'r') as file:
        minutes_2 = csv.reader(file)
        minutes2["fields"] = next(minutes_2)
        for row in minutes_2:
            row_list.append(tuple(row))
        minutes2["rows"] = row_list
            
    return minutes1, minutes2
minutes1,minutes2 = read_minutes() 
# print(minutes1,'\n', minutes2)


# Task 13: Create minutes_set            
def create_minutes_set():
    # set(minutes1['rows'])
    # set(minutes2['rows'])
    return set(minutes1['rows']).union(set(minutes2['rows']))
minutes_set = create_minutes_set()
print(minutes_set)


# Task 14: Convert to datetime
def create_minutes_list():
     date_list = list(minutes_set)
     lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y"))
     return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), date_list))

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
     minutes_list.sort(key = lambda x: x[1])
     conv_list =  list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
     with open('./minutes.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1['fields'])  # Write header row
        for row in conv_list:
            writer.writerow(row)
     return conv_list  