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
SELECT category, COUNT(*) AS times, SUM(amount) AS total
FROM expenses
WHERE amount <= 100
GROUP BY category
ORDER BY times DESC;
"""

cursor.execute(query)

results = cursor.fetchall()

print("\n===== SMALL EXPENSE PATTERN =====")

if results:
    for category, times, total in results:
        print(f"{category} → {times} small expenses → ₹{total}")
else:
    print("No small expenses found.")

cursor.close()
connection.close()

