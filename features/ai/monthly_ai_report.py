import os
import psycopg2
from dotenv import load_dotenv

load_dotenv(r'C:\Users\nikhi\Desktop\main.py\.env')
from datetime import date


connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cursor = connection.cursor()

current_month = date.today().replace(day=1)


print("\n===================================")
print("       MONTHLY SPENDING REPORT")
print("===================================")


# 1. Total spending
cursor.execute("""
    SELECT COALESCE(SUM(amount), 0)
    FROM expenses
    WHERE date >= %s;
""", (current_month,))

total = cursor.fetchone()[0]


# 2. Number of transactions
cursor.execute("""
    SELECT COUNT(*)
    FROM expenses
    WHERE date >= %s;
""", (current_month,))

transactions = cursor.fetchone()[0]


# 3. Highest spending category
cursor.execute("""
    SELECT category, SUM(amount) AS total
    FROM expenses
    WHERE date >= %s
    GROUP BY category
    ORDER BY total DESC
    LIMIT 1;
""", (current_month,))

category_result = cursor.fetchone()


# 4. Most-used payment method
cursor.execute("""
    SELECT payment_method, COUNT(*) AS times
    FROM expenses
    WHERE date >= %s
    GROUP BY payment_method
    ORDER BY times DESC
    LIMIT 1;
""", (current_month,))

payment_result = cursor.fetchone()


# 5. Highest spending day
cursor.execute("""
    SELECT date, SUM(amount) AS total
    FROM expenses
    WHERE date >= %s
    GROUP BY date
    ORDER BY total DESC
    LIMIT 1;
""", (current_month,))

day_result = cursor.fetchone()


# -------------------------------
# DISPLAY REPORT
# -------------------------------

print(f"\n📅 Month: {date.today().strftime('%B %Y')}")

print(f"💰 Total spending: ₹{total}")

print(f"🧾 Transactions: {transactions}")


if category_result:
    category, category_total = category_result

    print(
        f"🏆 Highest category: "
        f"{category} → ₹{category_total}"
    )


if payment_result:
    payment, payment_count = payment_result

    print(
        f"💳 Most used payment method: "
        f"{payment} → {payment_count} transactions"
    )


if day_result:
    highest_day, highest_total = day_result

    print(
        f"📅 Highest spending day: "
        f"{highest_day} → ₹{highest_total}"
    )


# -------------------------------
# SIMPLE AI-STYLE SUMMARY
# -------------------------------

print("\n===== MONTHLY INSIGHT =====")

if category_result:

    category, category_total = category_result

    percentage = (
        float(category_total) / float(total) * 100
        if float(total) > 0 else 0
    )

    print(
        f"This month, {category} was your highest "
        f"spending category."
    )

    print(
        f"It accounted for approximately "
        f"{percentage:.1f}% of your total spending."
    )


if transactions > 0:

    average = float(total) / transactions

    print(
        f"Your average expense per transaction "
        f"was approximately ₹{average:.2f}."
    )


print("\n===================================")
print("          END OF REPORT")
print("===================================")


cursor.close()
connection.close()
