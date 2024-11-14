import requests

from simulator.app.message_simulator.message_simulator import generate_message

DB_URL = 'http://localhost:5000/api/email'

def dispatch_email():
    for i in range(0, 300):
        print(i)
        is_dangerous = i % 3 == 0
        requests.post(DB_URL, json=generate_message(is_dangerous))
