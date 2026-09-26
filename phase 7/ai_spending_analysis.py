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


# Total spending
cursor.execute("""
    SELECT COALESCE(SUM(amount), 0)
    FROM expenses;
""")

total = cursor.fetchone()[0]


# Highest spending category
cursor.execute("""
    SELECT category, SUM(amount) AS total
    FROM expenses
    GROUP BY category
    ORDER BY total DESC
    LIMIT 1;
""")

highest_category = cursor.fetchone()


# Number of transactions
cursor.execute("""
    SELECT COUNT(*)
    FROM expenses;
""")

transactions = cursor.fetchone()[0]


print("\n===== AI SPENDING ANALYSIS =====")

print(f"\n💰 Total spending: ₹{total}")
print(f"🧾 Total transactions: {transactions}")


if highest_category:
    category, amount = highest_category

    print(f"🏆 Highest spending category: {category} → ₹{amount}")

    percentage = (float(amount) / float(total)) * 100

    print(f"📊 This category represents {percentage:.2f}% of your total spending.")


    if percentage >= 50:
        print(
            f"💡 Insight: A large portion of your spending "
            f"is going toward {category}."
        )

    elif percentage >= 30:
        print(
            f"💡 Insight: {category} is one of your major "
            f"spending areas."
        )

    else:
        print(
            f"💡 Insight: Your spending is relatively "
            f"distributed across categories."
        )


cursor.close()
connection.close()
