from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import csv
import json
import traceback
import time
import os
options = webdriver.ChromeOptions()

# Task 3

try:
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    
    look_elements = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")

    results = []
    
    for item in look_elements:
        try:
            title = item.find_element(By.CLASS_NAME, "title-content").text
            authors = item.find_elements(By.CLASS_NAME, "author-link")
            author_names = "; ".join([a.text for a in authors])
            format_info = item.find_element(By.CLASS_NAME, "display-info-primary").text  #display-info-primary
            book_dict = {
                "Title": title,
                "Author": author_names,
                "Format-Year": format_info
            }
            print(title)
            print(author_names)
            print(format_info)
            results.append(book_dict)    

        except Exception as e:
            print("Error in one item")
            traceback.print_exc()

    df = pd.DataFrame(results)
    print(df)

except Exception as e:
    print("Error")
    traceback.print_exc()

# Task 4

# Save extracted data to a CSV file
csv_path = os.path.join(".", "get_books.csv")
with open(csv_path, 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author", "Format-Year"])
    for book in results:
        writer.writerow([book["Title"], book["Author"], book["Format-Year"]])


# Save data to a JSON file
data = {"links": results}
with open('get_books.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)


driver.quit()    