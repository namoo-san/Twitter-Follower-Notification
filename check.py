# -*- coding:utf-8 -*-

import os
import requests

# Twitter API URL
BASE_URL = 'https://api.twitter.com/'
REQUEST_TOKEN_URL = BASE_URL + 'oauth/request_token'
AUTH_URL = BASE_URL + 'oauth/authenticate'
TOKEN_URL = BASE_URL + 'oauth/access_token'

# Twitter JSON URL
BASE_JSON_URL = 'https://api.twitter.com/1.1/%s.json'
TIMELINE_URL = BASE_JSON_URL % ('statuses/user_timeline')

def check_api_key():
    if 'TWITTER_API_KEY' in os.environ and 'TWITTER_API_SECRET' in os.environ and 'BEARER_TOKEN':
        API_KEY = os.environ['TWITTER_API_KEY']
        API_SECRET = os.environ['TWITTER_API_SECRET']
        BEARER_TOKEN = os.environ['BEARER_TOKEN']

        return {'API_KEY':API_KEY, 'API_SECRET':API_SECRET, 'BEARER_TOKEN':BEARER_TOKEN}
    else:
        print("Missing required parameters (API Key, API Secret, Bearer Token)")
        return

def main():
    credentials = check_api_key()
    for index, value in credentials.items():
        print(index, value)

if __name__ == "__main__":
    main()
