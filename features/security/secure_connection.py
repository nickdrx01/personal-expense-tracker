import os
import psycopg2
from dotenv import load_dotenv

# Load .env from the project folder
env_path = r"C:\Users\nikhi\Desktop\main.py\.env"
load_dotenv(env_path)

connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM expenses;")

count = cursor.fetchone()[0]

print("✅ Secure database connection successful!")
print(f"📊 Total expenses: {count}")

cursor.close()
connection.close()

print("🔒 Connection closed.")