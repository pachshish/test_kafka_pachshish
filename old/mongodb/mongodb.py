from pymongo import MongoClient

def get_mongo_client():
    # ניצור חיבור ל-MongoDB
    client = MongoClient("mongodb://localhost:27017/")
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
