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

category = input("Enter category to search: ")

query = """
SELECT * FROM expenses
WHERE category = %s
"""

cursor.execute(query, (category,))

expenses = cursor.fetchall()

if expenses:
    for expense in expenses:
        print(expense)
else:
    print("No expenses found ❌")

cursor.close()
connection.close()


