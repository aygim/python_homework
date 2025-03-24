# Task 2: Read a CSV File
import csv
value = "employees"
def read_employees ():
    emptyDict = {}
    row_list = []
    try:
        with open('../csv/employees.csv', newline='') as csvfile:
            csv_file_object = csv.reader(csvfile)
            emptyDict["fields"] = next(csv_file_object)
            for row in csv_file_object:
                    row_list.append(row)
            emptyDict["rows"] = row_list
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
