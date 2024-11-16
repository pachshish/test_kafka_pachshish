from sqlalchemy import Column, Integer, String, Float

from db import Base


class Explos(Base):
    __tablename__ = "suspicious_explosive_content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, index=True)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    city = Column(String)
    country = Column(String)
    browser = Column(String)
    os = Column(String)
    device_id = Column(String)
    sentences = Column(String, index=True)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'ip_address': self.ip_address,
            'created_at': self.created_at,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'city': self.city,
            'country': self.country,
            'browser': self.browser,
            'os': self.os,
            'device_id': self.device_id,
            'sentences': self.sentences
        }


