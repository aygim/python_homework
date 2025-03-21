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