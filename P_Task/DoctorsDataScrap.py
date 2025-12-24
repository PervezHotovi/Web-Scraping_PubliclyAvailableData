import json
import csv
from bs4 import BeautifulSoup

# Load saved HTML
with open("doctorsRecord.txt", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

scripts = soup.find_all("script", type="application/ld+json")

doctors = []

#making list of doctors if found
for script in scripts:
    try:
        json_text = script.get_text(strip=True)
        data = json.loads(json_text)

        # Case 1: Single object
        if isinstance(data, dict) and data.get("@type") == "Physician":
            doctors.append({
                "name": data.get("name"),
                "specialty": ", ".join(
                    s.get("name") for s in data.get("medicalSpecialty", [])
                ),
                "phone": data.get("telephone"),
                "email": data.get("email"),
                "url": data.get("url"),
                "priceRange": data.get("priceRange"),
                "description": data.get("description")
            })

        # Case 2: List of objects
        elif isinstance(data, list):
            for item in data:
                if item.get("@type") == "Physician":
                    doctors.append({
                        "name": item.get("name"),
                        "specialty": ", ".join(
                            s.get("name") for s in item.get("medicalSpecialty", [])
                        ),
                        "phone": item.get("telephone"),
                        "email": item.get("email"),
                        "url": item.get("url"),
                        "priceRange": item.get("priceRange"),
                        "description": item.get("description")
                    })

    except Exception as e:
        continue

print(f"Doctors found: {len(doctors)}")

# Write CSV
with open("doctors_apkamuaalij.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "specialty", "phone", "email", "url", "priceRange", "description"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(doctors)

print("CSV file created successfully.")
