import json
from kafka import KafkaConsumer

from pymongo import MongoClient

def get_mongo_client():
    # ניצור חיבור ל-MongoDB
    client = MongoClient("mongodb://mongodb:27017/")
    return client

def insert_all_messages(message):
    client = get_mongo_client()
    db = client["messages_db"]  # שם מסד הנתונים
    collection = db["all_messages"]  # שם הטבלה או הקולקציה
    collection.insert_one(message)
    print("Message inserted into MongoDB:", message)

def print_messages():
    client = get_mongo_client()
    db = client["messages_db"]
    collection = db["all_messages"]
    messages = collection.find()
    for message in messages:
        print(message)
print_messages()


consumer = KafkaConsumer(
    'all_messages_topic',
        bootstrap_servers='kafka:9092',
        auto_offset_reset = 'earliest',
        enable_auto_commit=True,
        group_id='emails'
)

for item in consumer:
    try:
        message = json.loads(item.value.decode('utf-8'))
        insert_all_messages(message)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Error processing message: {e}")
