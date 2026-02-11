import requests
from bs4 import BeautifulSoup
import pandas as pd
wiki_url = "https://en.wikipedia.org/wiki/Machine_learning"
request_headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(wiki_url, headers=request_headers)
if response.status_code != 200:
    print("Failed to fetch page:", response.status_code)
    exit()
soup = BeautifulSoup(response.text, "html.parser")
main_content_div = soup.find("div", id="mw-content-text")
if not main_content_div:
    print("Main content div not found")
    exit()
all_tables = main_content_div.find_all("table")
target_table = None
for table in all_tables:
    table_rows = table.find_all("tr")
    if len(table_rows) >= 4:
        target_table = table
        break
if not target_table:
    print("No suitable table found")
    exit()
header_row = target_table.find("tr")
header_cells = header_row.find_all("th")
if header_cells:
    table_headers = [th.get_text(strip=True) for th in header_cells]
else:
    max_columns = max(len(row.find_all(["td", "th"])) for row in target_table.find_all("tr"))
    table_headers = [f"col{i+1}" for i in range(max_columns)]
table_data = []
for tr in target_table.find_all("tr"):
    row_cells = tr.find_all(["td", "th"])
    row_data = [cell.get_text(strip=True) for cell in row_cells]
    while len(row_data) < len(table_headers):
        row_data.append("")
    if any(cell.strip() for cell in row_data):
        table_data.append(row_data)
df_table = pd.DataFrame(table_data[1:], columns=table_headers)
df_table.to_csv("wiki_table.csv", index=False)
print(f"Table saved to wiki_table.csv with {len(df_table)} rows and {len(df_table.columns)} columns.")