
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(r"C:\Users\nikhi\Desktop\main.py\.env")


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    payment_method = input("Enter payment method: ")

    try:
        connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

        cursor = connection.cursor()

        query = """
            INSERT INTO expenses
            (amount, category, description, payment_method)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (amount, category, description, payment_method)
        )

        connection.commit()

        print("Expense added successfully! ✅")

        cursor.close()
        connection.close()

    except Exception as e:
        print("Error ❌")
        print(e)

add_expense()


