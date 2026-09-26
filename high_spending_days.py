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
SELECT date, SUM(amount) AS total
FROM expenses
GROUP BY date
ORDER BY total DESC;
"""

cursor.execute(query)

results = cursor.fetchall()

print("\n===== HIGH-SPENDING DAYS =====")

if results:
    average = sum(total for date, total in results) / len(results)

    for date, total in results:
        if total > average:
            print(f"⚠️ {date} → ₹{total} (High spending)")
else:
    print("No expenses available.")

cursor.close()
connection.close()
