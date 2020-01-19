import tweepy
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("user", "user_secret")
auth.set_access_token("access", "access_secret")

# Create API object
api = tweepy.API(auth)

import requests

apiKey = "crypto_compare_api"

url = "https://min-api.cryptocompare.com/data/price"

payload = {
    "fsym": "BTC",
    "tsyms": "USD"
}

headers = {
    "authorization": "Apikey " + apiKey
}

result = requests.get(url, headers=headers, params=payload).json()
phrase = "The current BTC price is", result

print(phrase)

api.update_status(phrase)
