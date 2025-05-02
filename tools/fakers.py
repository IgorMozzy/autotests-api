import time
from string import ascii_letters
from random import choice, randint
from typing import Dict


def get_random_email() -> str:
    return f"test.{time.time()}@example.com"

def get_random_string() -> str:
    length = randint(5, 15)
    return "".join(choice(ascii_letters) for _ in range(length))

def get_fake_user_payload() -> Dict[str, str]:
    user_data = {
        "email": get_random_email(),
        "password": get_random_string(),
        "lastName": get_random_string(),
        "firstName": get_random_string(),
        "middleName": get_random_string()
    }
    return user_data