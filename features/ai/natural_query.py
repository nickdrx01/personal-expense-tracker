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


question = input("Ask about your expenses: ").lower()


if "food" in question:

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE LOWER(category) = 'food';
    """)

    total = cursor.fetchone()[0]

    print(f"\n💰 You spent ₹{total} on Food.")


elif "travel" in question:

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE LOWER(category) = 'travel';
    """)

    total = cursor.fetchone()[0]

    print(f"\n💰 You spent ₹{total} on Travel.")


elif "shopping" in question:

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE LOWER(category) = 'shopping';
    """)

    total = cursor.fetchone()[0]

    print(f"\n💰 You spent ₹{total} on Shopping.")


elif "entertainment" in question:

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE LOWER(category) = 'entertainment';
    """)

    total = cursor.fetchone()[0]

    print(f"\n💰 You spent ₹{total} on Entertainment.")


else:
    print("\n❌ I don't understand that question yet.")


cursor.close()
connection.close()
