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
    payment_method,
    COUNT(*) AS transactions,
    SUM(amount) AS total
FROM expenses
GROUP BY payment_method
ORDER BY total DESC;
"""

cursor.execute(query)

results = cursor.fetchall()

print("\n===== PAYMENT PATTERNS =====")

for method, transactions, total in results:
    print(
        f"{method} → "
        f"{transactions} transactions → "
        f"₹{total}"
    )

cursor.close()
connection.close()
