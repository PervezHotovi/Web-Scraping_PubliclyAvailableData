import requests
from bs4 import BeautifulSoup
url="https://sda.com.pk"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}

web= requests.get(url=url, headers=headers)
# print(web)
text=web.content
# t=type(web.content)
# print(text)

soup=BeautifulSoup(web.content,"html.parser")
tag=soup.find_all()
print(tag)

print(soup.title)
# with open("googleScrapFile.txt","wb") as file:
#     file.write(text)