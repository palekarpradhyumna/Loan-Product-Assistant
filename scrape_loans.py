import requests
from bs4 import BeautifulSoup

urls = [
    "https://bankofmaharashtra.in/personal-banking/loans/home-loan",
    "https://bankofmaharashtra.in/personal-banking/loans/personal-loan"
]

def fetch_loan_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all(['p', 'li'])
    return "\n".join([p.get_text(strip=True) for p in paragraphs])

all_data = ""
for url in urls:
    all_data += fetch_loan_data(url) + "\n\n"

with open("loan_data_raw.txt", "w", encoding="utf-8") as file:
    file.write(all_data)
