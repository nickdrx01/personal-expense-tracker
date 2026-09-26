import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(r"C:\Users\nikhi\Desktop\main.py\.env")


def test_database_connection():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    assert connection is not None

    connection.close()


def test_expenses_table_exists():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables
            WHERE table_name = 'expenses'
        );
    """)

    result = cursor.fetchone()[0]

    assert result is True

    cursor.close()
    connection.close()