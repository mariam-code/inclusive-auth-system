import random

def generate_otp():
    return str(random.randint(100000, 999999))

import requests

def log_event(message):
    try:
        requests.post("http://localhost:5002/log", json={"event": message})
    except Exception as e:
        print(f"Logging failed: {e}")
