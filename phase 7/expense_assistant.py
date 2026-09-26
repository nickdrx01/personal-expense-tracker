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
print("        💰 EXPENSE ASSISTANT")
print("===================================")

question = input("\nAsk me about your expenses: ").lower()


# Total spending
if "total" in question or "spent" in question:

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses;
    """)

    total = cursor.fetchone()[0]

    print(f"\n💰 Your total spending is ₹{total}")


# Highest spending category
elif "highest category" in question or "most spending" in question:

    cursor.execute("""
        SELECT category, SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        LIMIT 1;
    """)

    result = cursor.fetchone()

    if result:
        category, amount = result
        print(f"\n🏆 Highest spending category: {category}")
        print(f"💰 Amount: ₹{amount}")
    else:
        print("\nNo expense data available.")


# Food
elif "food" in question:

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE LOWER(category) = 'food';
    """)

    total = cursor.fetchone()[0]

    print(f"\n🍔 Food spending: ₹{total}")


# Travel
elif "travel" in question:

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE LOWER(category) = 'travel';
    """)

    total = cursor.fetchone()[0]

    print(f"\n🚗 Travel spending: ₹{total}")


# Shopping
elif "shopping" in question:

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE LOWER(category) = 'shopping';
    """)

    total = cursor.fetchone()[0]

    print(f"\n🛍️ Shopping spending: ₹{total}")


# Transaction count
elif "transaction" in question or "number of expenses" in question:

    cursor.execute("""
        SELECT COUNT(*)
        FROM expenses;
    """)

    count = cursor.fetchone()[0]

    print(f"\n🧾 Total transactions: {count}")


# Help
elif "help" in question:

    print("""
    
You can ask:

• How much did I spend?
• What is my total spending?
• Which category has highest spending?
• How much did I spend on food?
• How much did I spend on travel?
• How much did I spend on shopping?
• How many transactions do I have?

    """)


else:

    print("\n❌ I don't understand that question yet.")
    print("💡 Type 'help' to see available questions.")


cursor.close()
connection.close()

print("\n===================================")
print("       END OF ASSISTANT")
print("===================================")
