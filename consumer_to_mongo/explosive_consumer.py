import json

from kafka import KafkaConsumer, KafkaProducer
import time

from db import session
from models.explosive_model import Explos

#
consumer_p = KafkaConsumer(
    'topic_explosive',
    bootstrap_servers='localhost:9092',  # broker
    group_id='group_message',
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
def add_message_to_data(data):
    sentences = data['sentences']
    new_sen = ""
    for i in sentences:
        new_sen += i
    new_sen.replace('.', ' ')
    new_Hos = Explos(email=data['email'], username=data['username'],
                      ip_address=data['ip_address'], created_at=data['created_at'],
                      latitude=data['location']['latitude'], longitude=data['location']['longitude'], city=data['location']['city'],
                      country=data['location']['country'], browser=data['device_info']['browser'], os=data['device_info']['os'],
                      device_id=data['device_info']['device_id'],
                      sentences=new_sen)

    session.add(new_Hos)
    session.commit()

print("Consumer started, waiting for messages...")

for message in consumer_p:
    message_str = message.value
    print(f"Consumer_P received message: {message.value}")
    add_message_to_data(message_str)

    try:
        consumer_p.commit()
        print("Offset committed successfully.")
    except Exception as e:
        print(f"Error committing offset: {e}")

    time.sleep(1)
