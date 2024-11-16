import json

from kafka import KafkaConsumer

from old.flask_and_postgres.dangerous_db import db_session
from old.flask_and_postgres.emailModel import EmailModel, HostageModel, ExplosiveModel

consumer = KafkaConsumer(
    'dangerous_messages_topic',
        bootstrap_servers='localhost:9092',
        auto_offset_reset = 'earliest',
        enable_auto_commit=True,
        group_id='emails'
)

for item in consumer:
    message = json.loads(item.value.decode('utf-8'))
    data = message['sentences']
    data.split('.')
    for word in data:
        if "hostage" in word:
            email = EmailModel(
                email=message['email'],
                id_address=message['id_address'],
                created_at=message['created_at'],
                location=json.dumps(message['location']),
                device_info=json.dumps(message['device_info']),
                sentences=word
            )
            db_session.add(email)
            db_session.commit()
            email_id = email.id
            hostage = HostageModel(
                email_id=email_id
            )
            db_session.add(hostage)
            db_session.commit()

        elif "explosive" in word:
            email = EmailModel(
                email=message['email'],
                id_address=message['id_address'],
                created_at=message['created_at'],
                location=json.dumps(message['location']),
                device_info=json.dumps(message['device_info']),
                sentences=word
            )
            db_session.add(email)
            db_session.commit()
            email_id = email.id
            explosive = ExplosiveModel(
                email_id=email_id
            )
            db_session.add(explosive)
            db_session.commit()
