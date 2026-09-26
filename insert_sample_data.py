import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(r'C:\Users\nikhi\Desktop\main.py\.env')

connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cursor = connection.cursor()

query = """
INSERT INTO expenses
(amount, category, description, date, payment_method)
VALUES
(80, 'Food', 'Breakfast', '2026-09-01', 'UPI'),
(120, 'Food', 'Lunch', '2026-09-01', 'UPI'),
(60, 'Travel', 'Bus fare', '2026-09-01', 'Cash'),
(150, 'Food', 'Dinner', '2026-09-02', 'UPI'),
(50, 'Food', 'Tea and snacks', '2026-09-02', 'Cash'),
(200, 'Entertainment', 'Movie ticket', '2026-09-03', 'UPI'),
(90, 'Travel', 'Auto fare', '2026-09-03', 'Cash'),
(75, 'Food', 'Snacks', '2026-09-04', 'UPI'),
(100, 'Food', 'Lunch', '2026-09-04', 'UPI'),
(500, 'Shopping', 'Clothes', '2026-09-05', 'UPI'),
(70, 'Food', 'Breakfast', '2026-09-06', 'Cash'),
(110, 'Food', 'Lunch', '2026-09-06', 'UPI'),
(80, 'Travel', 'Bus fare', '2026-09-06', 'Cash'),
(1000, 'Education', 'Course fee', '2026-09-07', 'UPI'),
(90, 'Food', 'Dinner', '2026-09-08', 'UPI'),
(85, 'Food', 'Snacks', '2026-09-08', 'UPI'),
(300, 'Entertainment', 'Game', '2026-09-10', 'UPI'),
(120, 'Food', 'Lunch', '2026-09-10', 'UPI'),
(60, 'Food', 'Tea', '2026-09-10', 'Cash'),
(250, 'Shopping', 'Shoes', '2026-09-12', 'UPI')
"""

cursor.execute(query)
connection.commit()

print("20 sample expenses inserted successfully! ✅")

cursor.close()
connection.close()
