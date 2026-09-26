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
SELECT MAX(amount), MIN(amount)
FROM expenses
"""

cursor.execute(query)

result = cursor.fetchone()

highest = result[0]
lowest = result[1]

print("\n===== HIGHEST & LOWEST EXPENSE =====")
print("Highest Expense:", highest)
print("Lowest Expense :", lowest)

cursor.close()
connection.close()

