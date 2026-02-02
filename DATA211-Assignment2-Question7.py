import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
headers = {"User-Agent": "Mozilla/5.0"}  # Pretend we're a browser
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("Failed to fetch the page:", response.status_code)
    exit()
soup = BeautifulSoup(response.text, "html.parser")
if soup.title and soup.title.string:
    page_title = soup.title.string.strip()
    print(f"Page Title: {page_title}")
else:
    print("Page title not found")
content_div = soup.find("div", id="mw-content-text")
if content_div:
    paragraphs = content_div.find_all("p")
    for para in paragraphs:
        text = para.get_text().strip()
        if len(text) >= 50:
            print("\nFirst Paragraph:")
            print(text)
            break
else:
    print("Main content div not found")