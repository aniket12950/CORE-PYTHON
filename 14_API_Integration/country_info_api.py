"""
Project: Country Information Finder
API Used: REST Countries API
Description: Fetch country details like capital, population, currency, and flag
"""

import requests

def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()[0]

        country = data.get("name", {}).get("common", "N/A")
        capital = data.get("capital", ["N/A"])[0]
        population = data.get("population", "N/A")
        region = data.get("region", "N/A")
        currency = list(data.get("currencies", {}).values())[0]["name"] \
            if data.get("currencies") else "N/A"
        flag = data.get("flags", {}).get("png", "N/A")

        print("\n Country Details")
        print("-" * 30)
        print(f"Country     : {country}")
        print(f"Capital     : {capital}")
        print(f"Region      : {region}")
        print(f"Population  : {population}")
        print(f"Currency    : {currency}")
        print(f"Flag URL    : {flag}")

    except requests.exceptions.HTTPError:
        print(" Country not found.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("=== Country Information Finder ===")
    user_input = input("Enter country name: ")
    get_country_info(user_input.strip())
