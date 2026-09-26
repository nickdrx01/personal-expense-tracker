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
SELECT id, amount, category, description, date, payment_method
FROM expenses
WHERE LOWER(category) = LOWER(%s);
"""


cursor.execute(query, (category,))

results = cursor.fetchall()


print("\n===== SEARCH RESULTS =====")

if results:
    for expense in results:
        print(expense)
else:
    print("No expenses found.")


cursor.close()
connection.close()
