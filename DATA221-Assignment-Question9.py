import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Failed to fetch page:", response.status_code)
    exit()
soup = BeautifulSoup(response.text, "html.parser")
content_div = soup.find("div", id="mw-content-text")
if not content_div:
    print("Main content div not found")
    exit()
tables = content_div.find_all("table")
target_table = None
for table in tables:
    rows = table.find_all("tr")
    if len(rows) >= 4:
        target_table = table
        break
if not target_table:
    print("No suitable table found")
    exit()
header_row = target_table.find("tr")
th_tags = header_row.find_all("th")

if th_tags:
    headers = [th.get_text(strip=True) for th in th_tags]
else:
    cols_count = max(len(row.find_all(["td", "th"])) for row in target_table.find_all("tr"))
    headers = [f"col{i+1}" for i in range(cols_count)]
data = []
for tr in target_table.find_all("tr"):
    cells = tr.find_all(["td", "th"])
    row = [cell.get_text(strip=True) for cell in cells]
    while len(row) < len(headers):
        row.append("")
    if any(cell.strip() for cell in row):
        data.append(row)
df = pd.DataFrame(data[1:], columns=headers)
df.to_csv("wiki_table.csv", index=False)

print(f"Table saved to wiki_table.csv with {len(df)} rows and {len(df.columns)} columns.")