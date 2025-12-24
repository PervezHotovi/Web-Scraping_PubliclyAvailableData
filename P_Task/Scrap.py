from duckduckgo_search import DDGS

query = "Dental specialist in Pakistan"

urls = []

with DDGS() as ddgs:
    for r in ddgs.text(query, max_results=5):
        urls.append(r["href"])

print(urls)





trusted_keywords = ["hospital", "clinic", "university", "dental"]

filtered_urls = [
    url for url in urls
    if any(word in url.lower() for word in trusted_keywords)
]

print(filtered_urls)



import requests
from bs4 import BeautifulSoup
import time
import re

headers = {
    "User-Agent": "Mozilla/5.0 (educational research)"
}



doctors = []

for url in filtered_urls:
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup.find_all(["h1", "h2", "h3"]):
            name = tag.get_text(strip=True)

            if name.lower().startswith("dr"):
                doctors.append({
                    "name": name,
                    "qualification": "Not listed",
                    "source": url
                })

        time.sleep(2)

    except Exception as e:
        continue





unique_doctors = {
    (d["name"], d["qualification"]): d
    for d in doctors
}.values()

for d in unique_doctors:
    print(d)






import csv

with open("dental_specialists_pk.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["name", "qualification", "source"]
    )
    writer.writeheader()
    writer.writerows(unique_doctors)

