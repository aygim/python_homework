import os
import pandas as pd
import sqlite3


with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """
    SELECT l.line_item_id, l.quantity, l.product_id AS line_item_product_id, p.product_name, p.price 
    FROM line_items l JOIN products p ON l.product_id = p.product_id
    """
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head(5))

#Add a column to the DataFrame called "total".This is the quantity times the price.
df['total'] = df['quantity'] * df['price']
print('\nadding column total:')
print((df.head(5)))

# Add groupby() code to group by the product_id. 
# Use an agg() method that specifies 'count' for the line_item_id column, 'sum' for the total column, and 'first' for the 'product_name'
df_grouped=df.groupby('line_item_product_id').agg({
   'line_item_id' :'count',
   'total' : 'sum',
   'product_name' : 'first'
   })
print('\ngroup by the product_id:')
print(df_grouped.head(5))

# Sort the DataFrame by the product_name column.
df_sorted = df_grouped.sort_values(by='product_name')
print(df_sorted.head(5))

df_sorted.to_csv('assignment7/order_summary.csv', index=False)
print(df_sorted.head(5))