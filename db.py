import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DATABASE_URL = "postgresql://postgres:1234@localhost/kafka_test_message"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()


def check_db_connection():
    try:
        conn = psycopg2.connect(
            dbname='kafka_test_message',
            user='postgres',
            password='1234',
            host='localhost',
            port='5432'
        )
        conn.close()
        print("Connection to database is successful.")
    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
        exit(1)


