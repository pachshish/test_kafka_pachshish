from flask import Blueprint, request, jsonify
import json
from kafka import KafkaProducer


from service.consumer_service import check_email, change_senteness

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
bp_email = Blueprint('email', __name__)


@bp_email.route('/api/email', methods=['POST'])
def get_email():
    data = request.get_json()
    producer.send('topic_mes_all',value=data)
    print("send to message all")
    result = check_email(data)
    new_data = change_senteness(data)
    if result == "hostage":
        producer.send('topic_hostage', value=new_data)
    if result == "explosive":
        producer.send('topic_explosive', value=new_data)

    return jsonify({'message': 'Email sent successfully'}), 200
