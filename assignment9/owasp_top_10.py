from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import csv

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

def task6():
    driver = get_driver()
    driver.get("https://owasp.org/www-project-top-ten/")

    vulnerabilities_items = driver.find_elements(By.XPATH, "//ul/li/a[strong]")
    # By.CSS_SELECTOR, "ul.results > li.row.cp-search-result-item"
    print(f"Found {len(vulnerabilities_items)} vulnerability entries.")

    results = []
    for item in vulnerabilities_items:
        try:
            # print(item.get_attribute("innerHTML"))
            title = item.text
            href = item.get_attribute("href")
            results.append({'title': title, 'link': href})
        except Exception as e:
            print(f"Skipping entry due to error: {e}")
            
    driver.quit()

    for item in results:
        print(item)

    csv_path = os.path.join(".", "get_vulnerabilities.csv")
    with open(csv_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link"])
        writer.writeheader()
        writer.writerows(results)
    print(f"CSV written to: {csv_path}")

if __name__ == "__main__":
    task6()