import requests
from bs4 import BeautifulSoup

wiki_url = "https://en.wikipedia.org/wiki/Data_science"
request_headers = {"User-Agent": "Mozilla/5.0"}  # Pretend we're a browser
response = requests.get(wiki_url, headers=request_headers)
if response.status_code != 200:
    print("Failed to fetch the page:", response.status_code)
    exit()
soup = BeautifulSoup(response.text, "html.parser")
if soup.title and soup.title.string:
    page_title_text = soup.title.string.strip()
    print(f"Page Title: {page_title_text}")
else:
    print("Page title not found")
main_content_div = soup.find("div", id="mw-content-text")
if main_content_div:
    paragraph_elements = main_content_div.find_all("p")
    for paragraph in paragraph_elements:
        paragraph_text = paragraph.get_text().strip()
        if len(paragraph_text) >= 50:
            print("\nFirst Paragraph:")
            print(paragraph_text)
            break
else:
    print("Main content div not found")