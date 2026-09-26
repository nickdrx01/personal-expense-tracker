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

print("\n===== SMART SPENDING INSIGHTS =====")

# 1. Highest spending category
cursor.execute("""
    SELECT category, SUM(amount) AS total
    FROM expenses
    GROUP BY category
    ORDER BY total DESC
    LIMIT 1;
""")

result = cursor.fetchone()

if result:
    category, total = result
    print(f"\n💰 Highest spending category: {category} → ₹{total}")


# 2. Most frequently used payment method
cursor.execute("""
    SELECT payment_method, COUNT(*) AS transactions
    FROM expenses
    GROUP BY payment_method
    ORDER BY transactions DESC
    LIMIT 1;
""")

result = cursor.fetchone()

if result:
    method, transactions = result
    print(
        f"💳 Most used payment method: "
        f"{method} → {transactions} transactions"
    )


# 3. Money leak detection
cursor.execute("""
    SELECT
        category,
        description,
        COUNT(*) AS times,
        SUM(amount) AS total
    FROM expenses
    WHERE amount <= 100
    GROUP BY category, description
    HAVING COUNT(*) >= 2
    ORDER BY total DESC
    LIMIT 3;
""")

results = cursor.fetchall()

print("\n🔎 Potential money leaks:")

if results:
    for category, description, times, total in results:
        print(
            f"⚠️ {description} "
            f"({category}) → {times} times → ₹{total}"
        )
else:
    print("No potential money leaks detected.")


# 4. Highest spending day
cursor.execute("""
    SELECT date, SUM(amount) AS total
    FROM expenses
    GROUP BY date
    ORDER BY total DESC
    LIMIT 1;
""")

result = cursor.fetchone()

if result:
    date, total = result
    print(
        f"\n📅 Highest spending day: "
        f"{date} → ₹{total}"
    )


print("\n===== END OF INSIGHTS =====")

cursor.close()
connection.close()
