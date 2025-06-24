import sqlite3

def get_connection():
    try:
        return sqlite3.connect("mlb_scraper_project/mlb_data.db")
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def show_menu():
    print("\n Choose a query:")
    print("1. Top hitters by year")
    print("2. Players with AVG above a threshold")
    print("3. Players from a specific team")
    print("4. Year summary (total players and average AVG)")
    print("5. Exit")

def query_top_hitters_by_year(conn):
    try:
        year = input("Enter year (e.g., 2023): ").strip()
        cursor = conn.execute(
            "SELECT player, league, avg FROM batting_avg_leaders WHERE year = ? ORDER BY avg DESC",
            (year,))
        results = cursor.fetchall()
        if results:
            print(f"\nTop hitters in {year}:")
            for row in results:
                print(f"{row[0]} ({row[1]}) — AVG: {row[2]}")
        else:
            print("No results found.")
    except Exception as e:
        print(f"Error: {e}")

def query_avg_threshold(conn):
    try:
        threshold = float(input("Enter AVG threshold (e.g., 0.33): ").strip())
        cursor = conn.execute(
            "SELECT year, player, avg FROM batting_avg_leaders WHERE avg >= ? ORDER BY avg DESC",
            (threshold,))
        results = cursor.fetchall()
        if results:
            print(f"\nPlayers with AVG ≥ {threshold}:")
            for row in results:
                print(f"{row[1]} ({row[0]}) — AVG: {row[2]}")
        else:
            print("No players found.")
    except Exception as e:
        print(f"Error: {e}")

def query_team(conn):
    try:
        team = input("Enter team name (e.g., Miami): ").strip()
        cursor = conn.execute(
            "SELECT year, player, avg FROM batting_avg_leaders WHERE team LIKE ? ORDER BY year DESC",
            (f"%{team}%",))
        results = cursor.fetchall()
        if results:
            print(f"\nPlayers from team '{team}':")
            for row in results:
                print(f"{row[1]} ({row[0]}) — AVG: {row[2]}")
        else:
            print("No players found.")
    except Exception as e:
        print(f"Error: {e}")

def query_year_summary(conn):
    try:
        year = input("Enter year: ").strip()
        cursor = conn.execute(
            "SELECT COUNT(*), AVG(avg) FROM batting_avg_leaders WHERE year = ?",
            (year,))
        total, avg = cursor.fetchone()
        print(f"\nStats for {year}:")
        print(f"• Total players: {total}")
        print(f"• Average AVG: {avg:.3f}" if avg else "• Average AVG: not available")
    except Exception as e:
        print(f"Error: {e}")

def main():
    conn = get_connection()
    if not conn:
        return
    try:
        while True:
            show_menu()
            choice = input("Your choice: ").strip()
            if choice == "1":
                query_top_hitters_by_year(conn)
            elif choice == "2":
                query_avg_threshold(conn)
            elif choice == "3":
                query_team(conn)
            elif choice == "4":
                query_year_summary(conn)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()