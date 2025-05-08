import sqlite3   # For SQL command execution

conn = sqlite3.connect("../db/lesson.db",isolation_level='IMMEDIATE')
conn.execute("PRAGMA foreign_keys = 1")

cursor = conn.cursor()
#Task 1 Complex JOINs with Aggregation
cursor.execute("""
SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
FROM orders AS o
JOIN line_items AS li ON o.order_id = li.order_id
JOIN products AS p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
""")

results = cursor.fetchall()
print('\nTask 1 result:')
for row in results:
    print(row)

#Task 2: Understanding Subqueries
cursor.execute("""
SELECT c.customer_name, AVG(sub.total_price) AS average_total_price
FROM customers AS c
LEFT JOIN (SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
FROM orders AS o
JOIN line_items AS li ON o.order_id = li.order_id
JOIN products AS p ON p.product_id = li.product_id
GROUP BY o.order_id) AS sub
ON c.customer_id = sub.customer_id_b
GROUP BY c.customer_id;
""")

results = cursor.fetchall()
print('\nTask 2 result:')
for row in results:
    print(row)

#Task 3: An Insert Transaction Based on Data
try:
    cursor.execute("""
        SELECT customer_id 
        FROM customers 
        WHERE customer_name = ?""", ('Perez and Sons',))
    customer_id = cursor.fetchone()[0]

    cursor.execute("""
        SELECT employee_id
        FROM employees 
        WHERE first_name = ? AND last_name = ?""" , ('Miranda', 'Harris'))
    employee_id = cursor.fetchone()[0]

    cursor.execute("""
        SELECT product_id 
        FROM products 
        ORDER BY price ASC 
        LIMIT 5;
    """)
    results = cursor.fetchall()
    product_ids = [row[0] for row in results]

    print('\ncustomer_id:',customer_id)
    print('\nemployee_id:',employee_id)
    print('\nleast expensive products:')


#create the order record
    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?,?)
        RETURNING order_id;               
    """, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]
    print('\ncreated order with order_id:',order_id)

#insert 5 records in the line_items
    for product_id in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, ?)
    """, (order_id, product_id, 10))
    conn.commit()
    print("Order and line_items inserted successfully.")

#check results line_items
    cursor.execute("""
        SELECT li.line_item_id, li.quantity, li.order_id, p.product_name
        FROM line_items AS li
        JOIN products AS p ON li.product_id = p.product_id
        WHERE li.order_id = ?
    """, (order_id,))
    results = cursor.fetchall()
 
    print("\nInserted line items for the new order:")
    for row in results:
        print(row)

    conn.commit()

except Exception as e:
    conn.rollback()
    print(f"An error occurred: {e}")        


conn.close() 



import sqlite3   # For SQL command execution

conn = sqlite3.connect("../db/lesson.db",isolation_level='IMMEDIATE')
conn.execute("PRAGMA foreign_keys = 1")

cursor = conn.cursor()

# Task 4: Aggregation with HAVING
cursor.execute("""
SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING COUNT(o.order_id) > 5;
""")

results = cursor.fetchall()
print('\nTask 4 result:')
for row in results:
    print(row)