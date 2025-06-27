# <Web Scraping with BeautifulSoup>

import requests
from bs4 import BeautifulSoup


#1 - Scrape all headlines h1 from a news website.


#Send a Get request to website
url = "https://www.abpnews.com"
headers = {"User-Agent": "Mozilla/5.0"}   # Recommended: to avoid being blocked
response = requests.get(url, headers=headers)


#Parse html content using beautigulsoup
soup = BeautifulSoup(response.text,"html.parser")

#Extract headlines
headlines = soup.find_all('h1')

#Print headlines
print("Headlines -\n")
for i,headline in enumerate(headlines):
    print(f"{i+1}.{headline.text.strip()}")

