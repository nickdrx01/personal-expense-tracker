import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(r'C:\Users\nikhi\Desktop\main.py\.env')


connection = None
cursor = None

try:

    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = connection.cursor()

    print("✅ Database connected successfully!")


    # Test query
    cursor.execute("""
        SELECT COUNT(*)
        FROM expenses;
    """)

    count = cursor.fetchone()[0]

    print(f"📊 Total expenses: {count}")


    connection.commit()


except psycopg2.Error as error:

    print("\n❌ Database error occurred.")
    print("Error:", error)

    if connection:
        connection.rollback()
        print("🔄 Transaction rolled back.")


finally:

    if cursor:
        cursor.close()

    if connection:
        connection.close()
        print("🔒 Database connection closed.")
