from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from old.flask_and_postgres.emailModel import *

URI = 'postgresql://postgres:1234@localhost:5432/mydb'
#יצירת החיבור והרצת הדאטאבייס
#convert_unicode: עוזר להבין את השם של הURI גם אם יש שם סימנים בעייתים
engine = create_engine(URI)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def init_db():
    Base.metadata.create_all(bind=engine)