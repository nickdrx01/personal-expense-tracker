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
    date,
    SUM(amount) AS total
FROM expenses
GROUP BY date
ORDER BY date;
"""

cursor.execute(query)

results = cursor.fetchall()

print("\n===== SPENDING TREND =====")

previous = None

for date, total in results:
    print(f"{date} → ₹{total}")

    if previous is not None:
        if total > previous:
            print("  📈 Spending increased")
        elif total < previous:
            print("  📉 Spending decreased")
        else:
            print("  ➡️ Spending stayed same")

    previous = total

cursor.close()
connection.close()
