import requests
from bs4 import BeautifulSoup
import json

def scrape_msit():
    base_url = "https://www.msit.in"
    pages = ["/", "/admissions", "/aboutus", "/facilities", "/departments"]
    content_list = []

    for page in pages:
        try:
            res = requests.get(base_url + page)
            soup = BeautifulSoup(res.text, 'html.parser')
            paragraphs = soup.find_all('p')
            for p in paragraphs:
                text = p.get_text(strip=True)
                if len(text) > 50:
                    content_list.append(text)
        except Exception as e:
            print(f"Failed to fetch {page}: {e}")

    # Save directly as a list of strings
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(content_list, f, indent=2)

if __name__ == "__main__":
    scrape_msit()
