import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )


def add_expense():
    print("\n--- Add Expense ---")

    try:
        amount = float(input("Amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        category = input("Category: ").strip()
        description = input("Description: ").strip()
        payment_method = input("Payment Method: ").strip()

        if not category or not description or not payment_method:
            print("Fields cannot be empty.")
            return

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO expenses
        (amount, category, description, payment_method)
        VALUES (%s, %s, %s, %s);
        """

        cursor.execute(
            query,
            (amount, category, description, payment_method)
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")

    except psycopg2.Error as e:
        print("Database error:", e)


def view_expenses():
    print("\n--- All Expenses ---")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, amount, category, description, date, payment_method
            FROM expenses
            ORDER BY id;
        """)

        rows = cursor.fetchall()

        if not rows:
            print("No expenses found.")
        else:
            print("-" * 90)
            print(
                f"{'ID':<5}"
                f"{'Amount':<12}"
                f"{'Category':<15}"
                f"{'Description':<20}"
                f"{'Date':<15}"
                f"{'Payment':<10}"
            )
            print("-" * 90)

            for row in rows:
                print(
                    f"{row[0]:<5}"
                    f"₹{row[1]:<11.2f}"
                    f"{row[2]:<15}"
                    f"{row[3]:<20}"
                    f"{str(row[4]):<15}"
                    f"{row[5]:<10}"
                )

            print("-" * 90)

        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print("Database error:", e)


def update_expense():
    print("\n--- Update Expense ---")

    try:
        expense_id = int(input("Enter Expense ID: "))

        print("\n1. Amount")
        print("2. Category")
        print("3. Description")
        print("4. Payment Method")

        choice = input("Enter choice: ")

        conn = get_connection()
        cursor = conn.cursor()

        if choice == "1":
            amount = float(input("New amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                return

            cursor.execute(
                "UPDATE expenses SET amount = %s WHERE id = %s",
                (amount, expense_id)
            )

        elif choice == "2":
            category = input("New category: ").strip()

            cursor.execute(
                "UPDATE expenses SET category = %s WHERE id = %s",
                (category, expense_id)
            )

        elif choice == "3":
            description = input("New description: ").strip()

            cursor.execute(
                "UPDATE expenses SET description = %s WHERE id = %s",
                (description, expense_id)
            )

        elif choice == "4":
            payment = input("New payment method: ").strip()

            cursor.execute(
                "UPDATE expenses SET payment_method = %s WHERE id = %s",
                (payment, expense_id)
            )

        else:
            print("Invalid choice.")
            return

        if cursor.rowcount == 0:
            print("Expense ID not found.")
        else:
            conn.commit()
            print("Expense updated successfully!")

        cursor.close()
        conn.close()

    except ValueError:
        print("Please enter valid input.")

    except psycopg2.Error as e:
        print("Database error:", e)


def delete_expense():
    print("\n--- Delete Expense ---")

    try:
        expense_id = int(input("Enter Expense ID: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM expenses WHERE id = %s",
            (expense_id,)
        )

        if cursor.rowcount == 0:
            print("Expense ID not found.")
        else:
            conn.commit()
            print("Expense deleted successfully!")

        cursor.close()
        conn.close()

    except ValueError:
        print("Please enter a valid ID.")

    except psycopg2.Error as e:
        print("Database error:", e)


def search_expense():
    print("\n--- Search Expense ---")

    keyword = input("Search category or description: ").strip()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, amount, category, description, date, payment_method
            FROM expenses
            WHERE LOWER(category) LIKE LOWER(%s)
               OR LOWER(description) LIKE LOWER(%s)
            ORDER BY id;
        """, (f"%{keyword}%", f"%{keyword}%"))

        rows = cursor.fetchall()

        if not rows:
            print("No matching expenses found.")
        else:
            for row in rows:
                print(
                    f"ID: {row[0]} | "
                    f"₹{row[1]:.2f} | "
                    f"{row[2]} | "
                    f"{row[3]} | "
                    f"{row[4]} | "
                    f"{row[5]}"
                )

        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print("Database error:", e)


def expense_summary():
    print("\n--- Expense Summary ---")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                COALESCE(SUM(amount), 0),
                COUNT(*),
                COALESCE(AVG(amount), 0),
                COALESCE(MAX(amount), 0),
                COALESCE(MIN(amount), 0)
            FROM expenses;
        """)

        total, count, average, highest, lowest = cursor.fetchone()

        print(f"Total Expenses    : ₹{total:.2f}")
        print(f"Number of Expenses: {count}")
        print(f"Average Expense   : ₹{average:.2f}")
        print(f"Highest Expense   : ₹{highest:.2f}")
        print(f"Lowest Expense    : ₹{lowest:.2f}")

        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print("Database error:", e)


def main():
    while True:

        print("\n========================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("========================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Search Expense")
        print("6. Expense Summary")
        print("7. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            update_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            search_expense()

        elif choice == "6":
            expense_summary()

        elif choice == "7":
            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()