# import pandas as pd

# # Sample DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Age': [24, 27, 22, 32],
#         'Score': [85, 92, 88, 76]}
# df = pd.DataFrame(data)

# # Select the 'Name' column
# print("\n---Column---\n")
# print(df['Name'])

# # Select rows and specific columns
# print("\n---Rows and Columns---\n")
# print(df.loc[0:2, ['Name', 'Age']])

# # Select rows by position
# print("\n---Row by position---\n")
# print(df.iloc[:2])  # First two rows

# print("\n--the first 3 rows---\n")
# print(df.loc[0:2])  # This prints the first 3 rows! It starts with the row with index 0 and continues up to and including the row with index 2.
# print("\n---The first two rows only---\n")
# print(df.iloc[:2]) # This prints the first 2 rows only.  iloc[] works like list slicing.  It does not include the row with index 2.
# print("\n----Row 0 and 2---\n")
# print(df.loc[[0,2]]) # This prints row 0 and row 2.  You specify a list of the rows you want.  You can't do this with lists!

# print("\n--\n")
# print(df[df['Age'] > 24])
# # print(df[df['Age'] > 24 and df['Score'] >=88])         Doesn't work!  'and' is not a valid operator for Series!
# print("\n--\n")
# print(df[(df['Age'] > 24) & (df['Score'] >=88)])        # This one does work! It does the boolean AND of corresponding series elements.
# print("\n--\n")
# # print(df["a" in df['Name']])                          Doesn't work!  The "in" operator doesn't work for Series!
# print(df[df['Name'].str.contains("a")])                 # This does work!  
# # There are a bunch of useful str functions for Series.  While we're at it:
# # df['Name'] = df['Name'].upper()                       Doesn't work!!
# print("\n--\n")
# df['Name'] = df['Name'].str.upper()                     # Does work! 
# print(df)


# data = {'Category': ['A', 'B', 'A', 'B', 'C'],
#         'Values': [10, 20, 30, 40, 50]}
# df = pd.DataFrame(data)
# print("\n--data--\n", df)

# # Group by 'Category' and calculate the sum
# grouped = df.groupby('Category').sum()
# print(grouped) # grouped is another DataFrame with summary data

# # Calculate the mean for each group
# mean_values = df.groupby('Category')['Values'].mean()
# print(mean_values)


# import pandas as pd

# # Sample DataFrame
# data = {'Category': ['A', 'B', 'A', 'B', 'C'],
#         'Values': [10, 20, 30, 40, 50]}
# df = pd.DataFrame(data)
# print("\n---data\n", df)
# # Group by 'Category' and apply multiple aggregation functions
# result = df.groupby('Category').agg({'Values': ['sum', 'mean', 'count']})
# print(result)

# # Sample DataFrames
# df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
# df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [85, 92, 88]})
# print("\n--dataframes---\n", df1,"\n--2--\n", df2)

# # Merge on the 'ID' column
# merged_df = pd.merge(df1, df2, on='ID', how='inner')
# print("\n--merged dataframes--\n", merged_df)  # Inner merge

import pandas as pd

# Sample DataFrames

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
    'Name': ['Alice', 'Bob', 'Charlie']
})
print("\n---df1---\n", df1)
df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
    'Score': [85, 92, 88]
})
print("\n---df2---\n", df2)

# Merge on both 'ID' and 'Date'
merged_df = pd.merge(df1, df2, on=['ID', 'Date'], how='inner')
print("\n--merged ID and Date---\n", merged_df)

# Join DataFrames by index
df1 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']}, index=[1, 2, 3])
print("\n---df1---\n", df1)
df2 = pd.DataFrame({'Score': [85, 92, 88]}, index=[1, 2, 4])
print("\n---df2---\n", df2)
joined_df = df1.join(df2, how='outer')
print("\n--joined--\n", joined_df)

joined_df['bogus']=['x','y','z','w'] # adds a column
print("\n--add column--\n",joined_df)
joined_df['bogus']=joined_df['bogus'] + "_value"  # replaces a column
print("\n--replace column--\n", joined_df)
joined_df.drop('bogus', axis=1, inplace=True) # deletes the column.  You need axis=1 to identify that the drop is for a column, not a row
print("\n--deletes column--\n", joined_df)

import numpy
data = {'Name': ['A','B','C'],'Value':[1,2,3]}
new_df = pd.DataFrame(data)
print("\n---data---\n", new_df)

new_df['Value'] = new_df['Value'] ** 2  # using an operator
print("\n---using an operator---\n", new_df)

new_df['Value'] = numpy.sqrt(new_df['Value']) # using a numpy function.  You can't use math.sqrt() on a Series.
print("\n---using a numpy function---\n", new_df)

new_df['EvenOdd'] = new_df['Value'].map(lambda x : 'Even' if x % 2 == 0 else 'Odd') # the map method for a Series
print("\n---the map method---\n", new_df)

new_df['Value'] = new_df['Value'].astype(int) # type conversion method for a Series
print("\n---type conversion method---\n", new_df)

joined_df.rename(columns={'Score':'Test Score'}, inplace=True)
print("\n-rename column-\n", joined_df)

renamed_df=joined_df.set_index('Name')
print("\n-converting column to an index-\n", renamed_df)

joined_df.sort_values(by='Test Score',ascending=False,inplace=True)
print("\n-sort a DAtaframe by column values-\n", joined_df)

joined_df.reset_index(inplace=True, drop=True)
print("\n-to reset the index-\n", joined_df)