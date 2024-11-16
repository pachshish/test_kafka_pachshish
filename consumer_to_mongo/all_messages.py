import json

from kafka import KafkaConsumer, KafkaProducer
import time
from pymongo import MongoClient
MONGO_URI = 'mongodb://localhost:27017/'

DB_NAME = 'all_email'

COLLECTION_NAME = 'all_messages'




def get_collection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection

# Consumer קבלת הודעות מהנושא
consumer_p = KafkaConsumer(
    'messages.all',
    bootstrap_servers='localhost:9092',  # broker
    group_id='group_message_all',
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer started, waiting for messages...")

for message in consumer_p:
    message_str = message.value
    print(f"Consumer_P received message: {message.value}")
    conn = get_collection()
    conn.insert_one(message_str)

    try:
        consumer_p.commit()
        print("Offset committed successfully.")
    except Exception as e:
        print(f"Error committing offset: {e}")

    time.sleep(1)
