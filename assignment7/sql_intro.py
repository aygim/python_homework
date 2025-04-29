import sqlite3
import os

db_path = "../db/magazines.db"

try:
    with sqlite3.connect(db_path, isolation_level='IMMEDIATE') as conn:    
      conn.execute("PRAGMA foreign_keys = 1")
      print("Database connected successfully.")

    cursor = conn.cursor()

# Create Publisher table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)
# Create Magazines table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines (
        magazine_id INTEGER PRIMARY KEY,
        magazine_name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
    )
    """)
# Create Subscribers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)
# Create Subscriptions table    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id),
        FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id)           
    )
    """)

    print("Tables created successfully.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")





def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO Magazines (magazine_name,publisher_id) VALUES (?,?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.") 

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?,?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"{name},{address} are already in the database.")

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", 
                       (subscriber_id, magazine_id, expiration_date))
    except sqlite3.IntegrityError:
        print(f"Subscription for subscriber {subscriber_id} to magazine {magazine_id} already exists.")

# Adding sample data
add_publisher(cursor, 'Condé Nast')
add_publisher(cursor, 'Dotdash Meredith')
add_publisher(cursor, 'Hearst Corporation')

add_magazine(cursor,'Vogue', 1)
add_magazine(cursor,'People', 2)
add_magazine(cursor,'Cosmopolitan', 3)

add_subscriber(cursor, "John Walter", "123 Stallings Rd")
add_subscriber(cursor, "Alice Starski", "256 Ballantyne Rd")
add_subscriber(cursor, "Sergey Shostak", "695 Rockwell Rd")

add_subscription(cursor, 1, 2, "2025-12-31")
add_subscription(cursor, 1, 2, "2026-12-31")
add_subscription(cursor, 2, 1, "2025-11-30")

conn.commit()   
print('Sample data inserted succesfully')

#Write a query to retrieve all information from the subscribers table.
print("\nall subscribers:")
cursor.execute("SELECT * FROM Subscribers")
for row in cursor.fetchall():
    print(row)

# Write a query to retrieve all magazines sorted by name.
print("\nall magazines sorted by name:")
cursor.execute("SELECT * FROM Magazines ORDER BY magazine_name")
for row in cursor.fetchall():
    print(row)

# Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
print("\nMagazines published by Dotdash Meredith:")
cursor.execute("""
SELECT magazine_name 
FROM Magazines AS m
JOIN Publishers AS p ON m.publisher_id=p.publisher_id
WHERE p.name = 'Dotdash Meredith'
""")
for row in cursor.fetchall():
    print(row)
# Add these queries to your script. For each, print out all the rows returned by the query.