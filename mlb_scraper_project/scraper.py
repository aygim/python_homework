# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless") # Run browser in the background
options.add_argument("user-agent=Mozilla/5.0") # Set a fake user-agent

# Start the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# Wait up to 10 seconds for elements
wait = WebDriverWait(driver, 10)

try:
    # Go to the target webpage
    url = "https://www.baseball-almanac.com/hitting/hibavg3.shtml"
    driver.get(url)

    # Wait until the table is present
    table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

     # Get all rows except the header
    rows = table.find_elements(By.TAG_NAME, "tr")[1:]

    results = [] # Store the results here

    for row in rows:
        try:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 8:
                # American League data
                year_al = cells[0].text.strip()
                player_al = cells[1].text.strip()
                avg_al = cells[2].text.strip().split()[0]
                team_al = cells[3].text.strip()

                # National League data
                year_nl = cells[4].text.strip()
                player_nl = cells[5].text.strip()
                avg_nl = cells[6].text.strip().split()[0]
                team_nl = cells[7].text.strip()

                # Add both rows to results
                results.append([year_al, "AL", player_al, team_al, avg_al])
                results.append([year_nl, "NL", player_nl, team_nl, avg_nl])

        except Exception as row_error:
            print(f"Skipped row due to error: {row_error}")

finally:
    driver.quit() # Close the browser

try:
    # Save the results to CSV
    df = pd.DataFrame(results, columns=["Year", "League", "Player", "Team", "AVG"])
    df.to_csv("mlb_scraper_project/my_mlb_data.csv", index=False, encoding="utf-8")
    print("Saved my_mlb_data.csv")

except Exception as file_error:
    print(f"Error writing CSV: {file_error}")