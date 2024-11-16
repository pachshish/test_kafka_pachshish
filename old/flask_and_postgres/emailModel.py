from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


#תכונה שהופכת קלאסים לטבלאות
Base = declarative_base()



class EmailModel(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    id_address = Column(String(100))
    created_at = Column(String(100))
    location = Column(JSON)
    device_info = Column(JSON)
    sentences = Column(JSON)

class HostageModel(Base):
    __tablename__ = 'hostages'
    id = Column(Integer, primary_key=True)
    email_id = (Integer, ForeignKey('emails.id'))

class ExplosiveModel(Base):
    __tablename__ = 'explosives'
    id = Column(Integer, primary_key=True)
    email_id = (Integer, ForeignKey('emails.id'))