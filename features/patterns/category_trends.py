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
    DATE_TRUNC('month', date) AS month,
    SUM(amount) AS total
FROM expenses
GROUP BY category, month
ORDER BY category, month;
"""

cursor.execute(query)

results = cursor.fetchall()

print("\n===== CATEGORY TRENDS =====")

for category, month, total in results:
    print(f"{category} → {month.strftime('%B %Y')} → ₹{total}")

cursor.close()
connection.close()
