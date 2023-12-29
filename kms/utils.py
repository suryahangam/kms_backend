import time
import random


def generate_unique_ID():
    timestamp = int(time.time())
    random_number = random.randint(1, 1000)
    return f'{timestamp}{random_number}'

