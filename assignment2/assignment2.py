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