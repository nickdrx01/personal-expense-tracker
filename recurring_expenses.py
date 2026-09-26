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
SELECT category, description, COUNT(*) AS times
FROM expenses
GROUP BY category, description
HAVING COUNT(*) > 1
ORDER BY times DESC;
"""

cursor.execute(query)

results = cursor.fetchall()

print("\n===== RECURRING EXPENSES =====")

if results:
    for category, description, times in results:
        print(f"{category} → {description} → {times} times")
else:
    print("No recurring expenses found.")

cursor.close()
connection.close()
