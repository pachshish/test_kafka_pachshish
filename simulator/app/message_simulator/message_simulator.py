from faker.proxy import Faker
from typing import Dict
import random

fake = Faker()

danger_phrases = [
    'The explosives are set; detonation will occur at 3:00 AM sharp.',
    'Secure the location where the hostage will be kept. No loose ends.',
    'The package contains 5 kilos of explosives. Deploy it near the square.',
    'The hostage must remain blindfolded at all times to avoid identification.',
    'Ensure no traces are left after the explosion. Evacuate immediately.',
    'No harm should come to the hostage until we confirm the payment.',
    'The explosives must be placed near the foundation for maximum impact.',
    'Keep the hostage under constant surveillance to prevent escape.',
    'Check that all explosives are armed before leaving the site.',
    'The hostage’s restraints need to be checked every two hours.',
    'The explosion will act as the diversion. Be ready to move at 2:00 PM.',
    'We will release the hostage only after verifying the money transfer.',
    'All explosive materials are stored in the van. Handle with care.',
    'Ensure the hostage is kept in a soundproof room to avoid detection.',
    'The explosive device should be disguised as a regular package.',
    'Set the explosives timer for exactly 10 minutes after activation.',
    'The explosion will start the chain reaction. Make sure no one is nearby.'
]


def generate_message(is_dangerous: bool = False) -> Dict:
    fake_sentences = fake.sentences()
    random_index = random.randint(0, len(danger_phrases) - 1)
    return {
        'id': fake.uuid4(),
        'email': fake.email(),
        'username': fake.user_name(),
        'ip_address': fake.ipv4(),
        'created_at': fake.date_time_between(start_date='-30d', end_date='now').isoformat(),
        'location': {
            'latitude': float(fake.latitude()),
            'longitude': float(fake.longitude()),
            'city': fake.city(),
            'country': fake.country_code()
        },
        'device_info': {
            'browser': fake.user_agent(),
            'os': random.choice(['Windows', 'MacOS', 'Linux', 'iOS', 'Android']),
            'device_id': fake.uuid4()
        },
        'sentences': (
            fake_sentences if not is_dangerous
            else fake_sentences + [
                danger_phrases[random_index]
            ]
        )
    }
