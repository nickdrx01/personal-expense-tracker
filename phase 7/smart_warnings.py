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

print("\n===== SMART FINANCIAL WARNINGS =====")


# ------------------------------------------------
# 1. HIGH SPENDING CATEGORY
# ------------------------------------------------

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

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses;
    """)

    overall_total = cursor.fetchone()[0]

    percentage = (float(total) / float(overall_total)) * 100

    if percentage >= 40:
        print(
            f"\n⚠️ WARNING: {category} accounts for "
            f"{percentage:.1f}% of your total spending."
        )


# ------------------------------------------------
# 2. SMALL EXPENSES
# ------------------------------------------------

cursor.execute("""
    SELECT COUNT(*), COALESCE(SUM(amount), 0)
    FROM expenses
    WHERE amount <= 100;
""")

small_count, small_total = cursor.fetchone()

if small_count >= 5:
    print(
        f"\n🪙 WARNING: You made {small_count} "
        f"small purchases totaling ₹{small_total}."
    )


# ------------------------------------------------
# 3. HIGH-SPENDING DAY
# ------------------------------------------------

cursor.execute("""
    SELECT date, SUM(amount) AS total
    FROM expenses
    GROUP BY date
    ORDER BY total DESC
    LIMIT 1;
""")

result = cursor.fetchone()

if result:
    high_date, high_total = result

    cursor.execute("""
        SELECT COALESCE(AVG(daily_total), 0)
        FROM (
            SELECT SUM(amount) AS daily_total
            FROM expenses
            GROUP BY date
        ) AS daily;
    """)

    average_daily = cursor.fetchone()[0]

    if float(high_total) > float(average_daily) * 2:
        print(
            f"\n📈 WARNING: {high_date} had unusually high "
            f"spending of ₹{high_total}."
        )


# ------------------------------------------------
# 4. REPEATED EXPENSE
# ------------------------------------------------

cursor.execute("""
    SELECT category, description, COUNT(*) AS times
    FROM expenses
    GROUP BY category, description
    HAVING COUNT(*) >= 3
    ORDER BY times DESC
    LIMIT 1;
""")

result = cursor.fetchone()

if result:
    category, description, times = result

    print(
        f"\n🔁 WARNING: '{description}' was recorded "
        f"{times} times."
    )


print("\n===== END OF WARNINGS =====")


cursor.close()
connection.close()

