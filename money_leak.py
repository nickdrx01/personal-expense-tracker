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
SELECT
    category,
    description,
    COUNT(*) AS times,
    SUM(amount) AS total
FROM expenses
WHERE amount <= 100
GROUP BY category, description
HAVING COUNT(*) >= 2
ORDER BY total DESC;
"""

cursor.execute(query)

results = cursor.fetchall()

print("\n===== MONEY LEAK DETECTION =====")

if results:
    for category, description, times, total in results:
        print(
            f"⚠️ {category} → {description} → "
            f"{times} times → ₹{total}"
        )
else:
    print("No potential money leaks detected.")

cursor.close()
connection.close()

