#########################import#########################
import requests
from cachetools import cached, TTLCache

#########################CURRENCY_CONVERTE############################
# Define the cache with a max size of 200 items and a TTL of 5 minutes (300 seconds)
ttl_cache = TTLCache(maxsize=200, ttl=300)

# Function to get the exchange rate
@cached(ttl_cache)
def get_exchange_rate(base_currency, target_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url=url)
        if response.status_code != 200:
            return None
        data = response.json()
        exchange_rates = data.get("rates", "Not found")
        exchange_rate = exchange_rates.get(target_currency,"Not found")
        return exchange_rate
    except Exception as e:
        return e

# Function to convert the currency
def convert_currency(amount, exchange_rate):
    return amount * exchange_rate
######################################################################

if __name__ == "__main__":
    base_currency = input("Enter base currency: ")
    target_currency = input("Enter target currency: ")
    amount = int(input("Enter amount currency: "))
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    try:    
        amount_target_currency = convert_currency(amount, exchange_rate)
        print(f"{amount} {base_currency} is {amount_target_currency}{target_currency}.")
    except:
        print("An exception has occurred")
        print(exchange_rate)
    

