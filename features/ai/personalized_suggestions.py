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


print("\n===================================")
print("      PERSONALIZED SUGGESTIONS")
print("===================================")


# 1. Total spending
cursor.execute("""
    SELECT COALESCE(SUM(amount), 0)
    FROM expenses;
""")

total = float(cursor.fetchone()[0])


# 2. Highest spending category
cursor.execute("""
    SELECT category, SUM(amount) AS total
    FROM expenses
    GROUP BY category
    ORDER BY total DESC
    LIMIT 1;
""")

highest = cursor.fetchone()


# 3. Small frequent expenses
cursor.execute("""
    SELECT COUNT(*)
    FROM expenses
    WHERE amount <= 100;
""")

small_expenses = cursor.fetchone()[0]


# 4. Most used payment method
cursor.execute("""
    SELECT payment_method, COUNT(*) AS times
    FROM expenses
    GROUP BY payment_method
    ORDER BY times DESC
    LIMIT 1;
""")

payment = cursor.fetchone()


print("\n💡 YOUR SUGGESTIONS")


# Suggestion 1
if highest and total > 0:

    category, category_total = highest

    percentage = (float(category_total) / total) * 100

    if percentage >= 40:
        print(
            f"🔸 Consider monitoring your {category} spending. "
            f"It represents about {percentage:.1f}% of your total spending."
        )

    elif percentage >= 25:
        print(
            f"🔸 {category} is one of your major spending areas. "
            f"Keep an eye on it."
        )


# Suggestion 2
if small_expenses >= 5:

    print(
        f"🔸 You made {small_expenses} small expenses "
        f"(₹100 or less). These can add up over time."
    )


# Suggestion 3
if payment:

    method, count = payment

    print(
        f"🔸 {method} is your most frequently used payment method "
        f"({count} transactions)."
    )


# General suggestion
if total == 0:

    print("🔸 Add some expenses to receive personalized suggestions.")


print("\n===================================")
print("        END OF SUGGESTIONS")
print("===================================")


cursor.close()
connection.close()
