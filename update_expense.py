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

expense_id = int(input("Enter expense ID to update: "))
new_amount = float(input("Enter new amount: "))

query = """
UPDATE expenses
SET amount = %s
WHERE id = %s
"""

cursor.execute(query, (new_amount, expense_id))

connection.commit()

print("Expense updated successfully! ✅")

cursor.close()
connection.close()
