"""
Project: Crypto Price Tracker
API Used: CoinGecko Public API
Description: Fetch real-time cryptocurrency prices
"""

import requests
def get_crypto_price(coin_ids):
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    params = {
        "ids": ",".join(coin_ids),
        "vs_currencies": "usd,inr",
        "include_24hr_change": "true"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        for coin in coin_ids:
            if coin in data:
                print(f"\n🔹 {coin.upper()}")
                print(f"USD Price: ${data[coin]['usd']}")
                print(f"INR Price: ₹{data[coin]['inr']}")
                print(f"24h Change: {data[coin]['usd_24h_change']:.2f}%")
            else:
                print(f"{coin} not found.")
                
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)


if __name__ == "__main__":
    print("=== Crypto Price Tracker ===")
    user_input = input("Enter coin ids (comma separated, e.g., bitcoin,ethereum): ")
    
    coins = [coin.strip().lower() for coin in user_input.split(",")]
    get_crypto_price(coins)