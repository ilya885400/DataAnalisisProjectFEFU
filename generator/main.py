import os
import time
import random
import psycopg2
from datetime import datetime

# Настройки БД из переменных окружения
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('POSTGRES_DB', 'weather_db')
DB_USER = os.getenv('POSTGRES_USER', 'user')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'pass')

def connect_db():
    while True:
        try:
            conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
            return conn
        except Exception as e:
            print(f"Waiting for DB... {e}")
            time.sleep(2)

def init_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS weather_metrics (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                temperature FLOAT,
                humidity FLOAT,
                pressure FLOAT,
                wind_speed FLOAT,
                city VARCHAR(50)
            );
        """)
    conn.commit()

def generate_data():
    conn = connect_db()
    init_db(conn)
    cities = ['Moscow', 'Saint-Petersburg', 'Novosibirsk', 'Ekaterinburg']
    
    print("Generator started. Sending data...")
    while True:
        try:
            with conn.cursor() as cur:
                city = random.choice(cities)
                temp = round(random.uniform(-10.0, 30.0), 2)
                hum = round(random.uniform(30.0, 90.0), 2)
                press = round(random.uniform(740.0, 770.0), 2)
                wind = round(random.uniform(0.0, 15.0), 2)
                
                cur.execute(
                    "INSERT INTO weather_metrics (temperature, humidity, pressure, wind_speed, city) VALUES (%s, %s, %s, %s, %s)",
                    (temp, hum, press, wind, city)
                )
            conn.commit()
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            conn = connect_db()

if __name__ == "__main__":
    generate_data()
