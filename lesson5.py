import pandas as pd
data = [{'Employee': 'Jones', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9000}, \
{'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 4000}, \
{'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 11000}, \
{'Employee': 'Jones', 'Product': 'Widget', 'Region': 'East', 'Revenue': 4000}, \
{'Employee': 'Jones', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 5500}, \
{'Employee': 'Jones', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2345}, \
{'Employee': 'Smith', 'Product': 'Widget', 'Region': 'West', 'Revenue': 9007}, \
{'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 40003}, \
{'Employee': 'Smith', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 110012}, \
{'Employee': 'Smith', 'Product': 'Widget', 'Region': 'East', 'Revenue': 9002}, \
{'Employee': 'Smith', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 15500}, \
{'Employee': 'Garcia', 'Product': 'Widget', 'Region': 'West', 'Revenue': 6007}, \
{'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'West', 'Revenue': 42003}, \
{'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'West', 'Revenue': 160012}, \
{'Employee': 'Garcia', 'Product': 'Gizmo', 'Region': 'East', 'Revenue': 16500}, \
{'Employee': 'Garcia', 'Product': 'Doohickey', 'Region': 'East', 'Revenue': 2458}]
sales = pd.DataFrame(data)
print('\n',sales)
sales_pivot1 = pd.pivot_table(sales,index=['Product','Region'],values=['Revenue'],aggfunc='sum',fill_value=0)
print('\n',sales_pivot1)
# This creates a two level index to show sales by product and region. The revenue values are summed for each product and region.
sales_pivot2 = pd.pivot_table(sales,index='Product',values='Revenue',columns='Region', aggfunc='sum',fill_value=0)
print('\n',sales_pivot2)
# The result here is similar, but instead of a two level index, you have columns to give sales by region.
sales_pivot3 = pd.pivot_table(sales,index='Product',values='Revenue',columns=['Region','Employee'], aggfunc='sum',fill_value=0)
print('\n',sales_pivot3)
# By adding the employee column, you get these revenue numbers broken down by employee.  The fill value is used when there is no corresponding entry.

sales_pivot2['Total'] = sales_pivot2['East'] + sales_pivot2['West'] # adding two columns to make a new one
print('\n',sales_pivot2)
per_employee_sales=sales.groupby('Employee').agg({'Revenue':'sum'})
per_employee_sales['Commission Percentage'] = [0.12, 0.09, 0.1]
per_employee_sales['Commission'] = per_employee_sales['Revenue'] * per_employee_sales['Commission Percentage']
print('\n',per_employee_sales)

per_employee_sales=sales.groupby('Employee').agg({'Revenue':'sum'})
per_employee_sales['Commission Plan'] = ['A', 'A', 'B']
def calculate_commission(row):
    if row['Revenue'] < 10000:
        return 0
    if row['Commission Plan'] == 'A':
        return 1000 + 0.05 * (row['Revenue'] - 10000)
    else:
        return 1400 + 0.04 * (row['Revenue'] - 10000)

per_employee_sales['Commission'] = per_employee_sales.apply(calculate_commission, axis=1)
print('\n',per_employee_sales)

# Sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', None, 'David'],
        'Age': [24, 27, 22, None],
        'Score': [85, None, 88, 76]}
df = pd.DataFrame(data)
print('\n',df)

# Find rows with missing data
df_missing = df[df.isnull().any(axis=1)]
print('\n',df_missing)

# Remove rows with missing data
df_dropped = df.dropna()
print('\n',df_dropped)

# Replace missing data with default values
df_filled = df.fillna({'Age': 0, 'Score': df['Score'].mean()})
print('\n',df_filled)

# df.isnull().any(axis=1) finds the rows that have null or NaN values.  The axis=1 is needed to specify rows.
# dropna() removes any row that contains a None (missing) value. This can remove quite a lot of data, especially if you have a lot of columns.
# fillna() is used to replace missing values. 
# In this case, the Age column's missing values are replaced with 0, and the Score column's missing values are filled with the mean of the existing scores.
#  This can cause issues if the values you are replacing become outliers.

# Sample DataFrame with mixed data types
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': ['24', '27', '22'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)
print('\n',df )
print('\n', df.dtypes)
# Convert 'Age' column to integers
df['Age'] = df['Age'].astype(int)
# Convert 'JoinDate' column to datetime
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print('\n',df.dtypes)  # Verify data types
print('\n',df)

# In addition you can use the Series map() method to change items in a column.
# Sample DataFrame

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
df = pd.DataFrame(data)
print('\n', df)
print('\n',df.dtypes) 
# Convert 'Location' abbreviations into full names
df['Location'] = df['Location'].map({'LA': 'Los Angeles', 'NY': "New York"})
print('\n',df)

# The problem with the code above is that if the value in the 'Location' column is not either 'LA' or 'NY', it is converted to NaN.  
# Suppose you want to preserve the existing value in this case. You'd use the replace() method instead:
df['Location'] = df['Location'].replace({'LA': 'Los Angeles', 'NY': "New York"})

data = {'Name': ['Tom', 'Dick', 'Harry', 'Mary'], 'Phone': [3212347890, '(212)555-8888', '752-9103','8659134568']}
df = pd.DataFrame(data)
print('\n',df.dtypes) 

df['Correct Phone'] = df['Phone'].astype(str)
def fix_phone(phone):
    if phone.isnumeric():
        out_string = phone
    else:
        out_string = ''
        for c in phone:
            if c in '0123456789':
                out_string += c
    if len(out_string) == 10:
        return out_string
    return None
    
df['Correct Phone'] = df['Correct Phone'].map(fix_phone)
print('\n',df)

data = {'Name': ['Alice', 'Bob', 'Charlie'],
	'Age': [20, 22, 43]}

df = pd.DataFrame(data)

# Increase the age by 1 as a new year has passed
df['Age'] = df['Age'] + 1  # "="  ????? is ut bug in the lesson 5 materials???
print('\n',df)
# For Data Discretization we have to use the more complicated pandas.cut() function. 
# This will allow us to automatically split data into a series of equal sized bins.
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'Grade': [78, 40, 85]}
df = pd.DataFrame(data)
print('\n',df)
# Convert grade into three catagories, "bad", "okay", "great"

df['Grade'] = pd.cut(df['Grade'], 3, labels = ["bad", "okay", "great"])
print('\n',df)

# Explanation:

# astype(int) converts the Age column, originally stored as strings, into integers.
# pd.to_datetime() converts the JoinDate column into Python’s datetime objects for easier date manipulation and comparison.
# pd.cut() allows us to create bins for data and provide data discretization

# Example: Using drop_duplicates()]
# Sample DataFrame with duplicates
data = {'Name': ['Alice', 'Bob', 'Alice', 'David'],
        'Age': [24, 27, 24, 32],
        'Score': [85, 92, 85, 76]}
df = pd.DataFrame(data)
print('\n',df)
# Identify and remove duplicates
df_cleaned = df.drop_duplicates()
print('\n',df_cleaned)
# Remove duplicates based on 'Name' column
df_cleaned_by_name = df.drop_duplicates(subset='Name')
print('\n',df_cleaned_by_name)

Explanation:

# drop_duplicates() removes rows where the entire record is a duplicate of another.
# drop_duplicates(subset='Name') removes rows where the Name column is duplicated, keeping only the first occurrence of each name.

# Handling Outliers
# Code Example:# Replace outliers in 'Age' (e.g., Age > 100 or Age < 0)
# df['Age'] = df['Age'].apply(lambda x: df['Age'].median() if x > 100 or x < 0 else x)

# print("DataFrame after handling outliers:")
# print(df)
# Explanation:
# Outliers in the Age column that are greater than 100 or less than 0 are replaced by the median value of the Age column.


# jobs.columns = jobs.columns.str.strip()

# jobs.columns — это Index объект, содержащий все названия колонок в DataFrame jobs.

# .str.strip() — это метод для строк, который удаляет лишние пробелы в начале и в конце каждого названия колонки.


# # Пример с неаккуратными названиями колонок
# data = {
#     ' Name ': ['Alice', 'Bob'],
#     'AGE ': [25, 30],
#     ' Monthly Salary($) ': [50000, 60000]
# }

# df = pd.DataFrame(data)

# # Посмотрим на исходные названия
# print("До обработки:")
# print(df.columns.tolist())

# # Очистим названия: уберем пробелы, переведем в нижний регистр, заменим пробелы и скобки
# df.columns = (
#     df.columns
#     .str.strip()                      # убирает пробелы по краям
#     .str.lower()                     # переводит в нижний регистр
#     .str.replace(' ', '_')          # заменяет пробелы на подчёркивания
#     .str.replace('(', '')           # убирает открывающие скобки
#     .str.replace(')', '')           # убирает закрывающие скобки
# )

# # Проверим результат
# print("\nПосле обработки:")
# print(df.columns.tolist())
