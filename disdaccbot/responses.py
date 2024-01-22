from random import choice, randint
import requests
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