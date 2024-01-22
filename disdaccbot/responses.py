from random import choice, randint
import requests
from bs4 import BeautifulSoup
import validators
import json

def get_response(message: str, username: str) -> str:
    lower_message: str = message.lower()

    if lower_message == 'hello':
        return 'Hello, '+ username + '!'
    else:
        return choice([
            'I don\'t know what to say',
            'I\'m not sure what you mean',
            'I don\'t understand',
            'I\'m not sure what you\'re saying']) 

def get_random_quote(api_key: str) -> str:
    response = requests.get(api_key)
    quotes = response.json()['quotes']
    quote = quotes[randint(0,len(quotes)-1)]['quote']
    return quote

def read_json(path_to_json: str):
    try:
        with open(path_to_json, 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(e)
        return None

def get_random_challenge(path_to_json: str) -> str:
    data = read_json(path_to_json)
    challenge = choice(data['challenges'])
    return f'{challenge["name"]}: {challenge["url"]}'

def get_title(url: str) -> str:
    if not validators.url(url):
        return 'Invalid URL'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        url_title = soup.title.string
        return url_title.split('|')[0]
    except Exception as e:
        print(e)
        return 'Invalid URL'

def add_new_challenge(path_to_json: str, url: str) -> str:
    if get_title(url) == 'Invalid URL':
        return f'Unable to add: {url} please check if it is a valid Coding Challenge URL'
    data = read_json(path_to_json)
    for challenge in data['challenges']:
        if challenge['url'] == url:
            return f'URL already exists: {url}'
    data['challenges'].append({"name": get_title(url), "url": url})
    try:
        with open(path_to_json, 'w') as f:
            json.dump(data, f, indent=4)
        return f'Added: {get_title(url)}: {url}'
    except Exception as e:
        print(e)

def list_all_challenges(path_to_json: str) -> str:
    data = read_json(path_to_json)
    result = '\n'.join([f'{challenge["name"]}: {challenge["url"]}' for challenge in data['challenges']])
    try:
        #Discord has a 2000 character limit for messages so we need to split the result into chunks
        chunks = [result[i:i+2000] for i in range(0, len(result), 2000)]
        for chunk in chunks:
            return chunk
    except Exception as e:
        print(e)