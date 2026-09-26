import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(r"C:\Users\nikhi\Desktop\main.py\.env")

connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cursor = connection.cursor()

query = """
SELECT category, SUM(amount)
FROM expenses
GROUP BY category
ORDER BY SUM(amount) DESC
"""

cursor.execute(query)

results = cursor.fetchall()

print("\n===== CATEGORY-WISE SPENDING =====")

for category, total in results:
    print(category, ":", total)

cursor.close()
connection.close()