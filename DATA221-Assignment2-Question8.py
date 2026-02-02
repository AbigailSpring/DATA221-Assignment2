import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
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
headings = content_div.find_all("h2")
filtered_headings = []

for h2 in headings:
    text = h2.get_text().strip()
    text = text.replace("[edit]", "").strip()
    skip_words = ["References", "External links", "See also", "Notes"]
    if any(word in text for word in skip_words):
        continue
    filtered_headings.append(text)
with open("headings.txt", "w", encoding="utf-8") as f:
    for heading in filtered_headings:
        f.write(heading + "\n")
print("Extracted Headings:")
for heading in filtered_headings:
    print(heading)