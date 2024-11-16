from flask import Flask, request
from kafka import KafkaProducer

from old.flask_and_postgres.dangerous_db import init_db

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='localhost:9092')

URI = 'postgresql://postgres:1234@localhost:5432/mydb'

app.config["SQLALCHEMY_DATABASE_URI"] = URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

with app.app_context():
    init_db()

# get the data from the simulator
@app.route('/api/email', methods=['POST'])
def get_from_simulator():
    message = request.data
    producer.send('message.all', value=message)
    print(message)
    return 'Email Received!', 200


if __name__ == '__main__':
    app.run()
