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
    COUNT(*),
    COALESCE(SUM(amount), 0),
    COALESCE(AVG(amount), 0)
FROM expenses
"""

cursor.execute(query)

result = cursor.fetchone()

total_expenses = result[0]
total_amount = result[1]
average_amount = result[2]

print("\n===== EXPENSE SUMMARY =====")
print("Total Expenses :", total_expenses)
print("Total Spending :", total_amount)
print("Average Expense:", round(average_amount, 2))

cursor.close()
connection.close()
