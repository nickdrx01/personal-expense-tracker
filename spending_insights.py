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
SELECT category, SUM(amount) AS total
FROM expenses
GROUP BY category
ORDER BY total DESC
LIMIT 1;
"""

cursor.execute(query)

result = cursor.fetchone()

print("\n===== SPENDING INSIGHT =====")

if result:
    category, total = result

    print("Highest spending category:", category)
    print("Amount spent:", total)

    print(f"\n💡 Insight: You spent the most on {category}.")
else:
    print("No expenses available.")

cursor.close()
connection.close()
