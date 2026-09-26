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
    SUM(amount) AS category_total,
    ROUND(
        SUM(amount) * 100.0 / (SELECT SUM(amount) FROM expenses),
        2
    ) AS percentage
FROM expenses
GROUP BY category
ORDER BY percentage DESC;
"""

cursor.execute(query)

results = cursor.fetchall()

print("\n===== SPENDING PERCENTAGE =====")

for category, total, percentage in results:
    print(category, ":", total, "(", percentage, "%)")

cursor.close()
connection.close()
