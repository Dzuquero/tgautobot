
import time
from sqlalchemy import create_engine, text
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

sample_data = [
    {"brand": "BMW", "model": "X5", "year": 2019, "price": 1900000, "color": "red", "url": "url1"},
    {"brand": "Audi", "model": "A6", "year": 2018, "price": 1700000, "color": "black", "url": "url2"},
]

while True:
    with engine.begin() as conn:
        for car in sample_data:
            conn.execute(text("""
                INSERT INTO cars (brand, model, year, price, color, url)
                VALUES (:brand, :model, :year, :price, :color, :url)
                ON CONFLICT (url) DO UPDATE SET
                price = EXCLUDED.price,
                color = EXCLUDED.color
            """), car)
    time.sleep(600)
