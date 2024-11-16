# Dockerfile for Consumer saving fraud transactions to MongoDB

# השתמש בתמונה של Python
FROM python:3.9-slim

# הגדרת תיקיית העבודה
WORKDIR /app

# העתקת קובצי הפרויקט לתוך התמונה
COPY . /app

# התקנת התלויות
RUN pip install --no-cache-dir -r requirements.txt

# פקודת ריצה של הקוד
CMD ["python", "mongodb.py"]
