import sqlite3
import pandas as pd

try:
    # Load cleaned CSV
    df = pd.read_csv("mlb_scraper_project/my_mlb_data_cleaned.csv")

    # Connect to SQLite and create table
    with sqlite3.connect("mlb_scraper_project/mlb_data.db") as conn:
        cursor = conn.cursor()

        # Drop existing table if exists
        cursor.execute("DROP TABLE IF EXISTS batting_avg_leaders")

        # Create new table
        cursor.execute("""
            CREATE TABLE batting_avg_leaders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                year INTEGER,
                league TEXT,
                player TEXT,
                team TEXT,
                avg REAL
            )
        """)

        # Insert data row by row
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO batting_avg_leaders (year, league, player, team, avg)
                VALUES (?, ?, ?, ?, ?)
            """, (row["Year"], row["League"], row["Player"], row["Team"], row["AVG"]))


        conn.commit()
    print("Loaded data into mlb_data.db")

except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
    print(f"Error occurred: {e}")