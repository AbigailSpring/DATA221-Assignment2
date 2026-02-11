import requests
from bs4 import BeautifulSoup

wiki_url = "https://en.wikipedia.org/wiki/Data_science"
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
h2_elements = main_content_div.find_all("h2")
filtered_h2_headings = []
skip_headings = ["References", "External links", "See also", "Notes"]
for h2 in h2_elements:
    heading_text = h2.get_text().replace("[edit]", "").strip()
    if any(skip_word in heading_text for skip_word in skip_headings):
        continue
    filtered_h2_headings.append(heading_text)
with open("headings.txt", "w", encoding="utf-8") as output_file:
    for heading in filtered_h2_headings:
        output_file.write(heading + "\n")
print("Extracted Headings:")
for heading in filtered_h2_headings:
    print(heading)