import requests
import json
from datetime import datetime
import concurrent.futures
from cachetools import TTLCache

# Create a session object for making HTTP requests
session = requests.Session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Cache object for storing API responses
cache = TTLCache(maxsize=1, ttl=300)

# Get the current date and time
now = datetime.now()

# Format the date and time
formatted_date_time = now.strftime("Today %d %B, %I:%M %p")


def get_nifty50():
    if 'nifty50' in cache:
        return cache['nifty50']

    url = "https://query1.finance.yahoo.com/v7/finance/chart/%5ENSEI"
    response = session.get(url)

    try:
        data = response.json()
        regular_nifty_price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        cache['nifty50'] = regular_nifty_price
        return regular_nifty_price
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)


def get_sensex():
    url = "https://query1.finance.yahoo.com/v7/finance/chart/%5EBSESN"
    response = session.get(url)
    data = response.json()

    # Extract regularMarketPrice from the response
    regular_sensex_price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]

    return regular_sensex_price


def get_financial_news_headline():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d30476a43d0c4dce9eef4ddd1f6a7a9c"

    try:
        response = session.get(url)
        response.raise_for_status()  # Raise an exception if status code is not 2xx
        data = response.json()
        articles = data['articles']
        if articles:
            headline = articles[0]['title']
            return headline
        else:
            print("No financial news headlines found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def get_random_quote():
    url = "https://zenquotes.io/api/random"

    try:
        response = session.get(url)
        response.raise_for_status()  # Raise an exception if status code is not 2xx
        data = response.json()
        quote = data[0]['q'] + " - " + data[0]['a']
        return quote
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def get_financial_data():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        nifty50_future = executor.submit(get_nifty50)
        sensex_future = executor.submit(get_sensex)
        headline_future = executor.submit(get_financial_news_headline)

        nifty50 = nifty50_future.result()
        sensex = sensex_future.result()
        headline = headline_future.result()

    return nifty50, sensex, headline


if __name__ == '__main__':
    nifty50, sensex, headline = get_financial_data()

    print("\n\n")
    print("Today's Nifty 50:", nifty50)
    print(formatted_date_time)
    print("\n\n")
    print("BSE Sensex:", sensex)
    print(formatted_date_time)
    print("\n\n")

    if headline:
        print("Latest Financial News Headline:")
        print(headline)

    print("\n\n")
    print(get_random_quote())
