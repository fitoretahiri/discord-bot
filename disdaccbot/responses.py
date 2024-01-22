from random import choice, randint

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

