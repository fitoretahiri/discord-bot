from random import choice, randint
import requests

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

def get_random_quote() -> str:
    response = requests.get("https://dummyjson.com/quotes")
    quotes = response.json()['quotes']
    quote = quotes[randint(0,len(quotes)-1)]['quote']
    return quote