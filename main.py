
from datetime import datetime

expenses = []


def add_expense():
    print("\n--- Add Expense ---")

    try:
        amount = float(input("Amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input("Category: ").strip()
    description = input("Description: ").strip()
    payment_method = input("Payment Method: ").strip()

    if not category or not description or not payment_method:
        print("Category, description and payment method cannot be empty.")
        return

    expense = {
        "id": len(expenses) + 1,
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%d-%m-%Y"),
        "payment_method": payment_method
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    print("-" * 80)
    print(
        f"{'ID':<5}"
        f"{'Amount':<12}"
        f"{'Category':<15}"
        f"{'Description':<20}"
        f"{'Date':<15}"
        f"{'Payment':<10}"
    )
    print("-" * 80)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"₹{expense['amount']:<11.2f}"
            f"{expense['category']:<15}"
            f"{expense['description']:<20}"
            f"{expense['date']:<15}"
            f"{expense['payment_method']:<10}"
        )

    print("-" * 80)


def update_expense():
    print("\n--- Update Expense ---")

    if not expenses:
        print("No expenses found.")
        return

    try:
        expense_id = int(input("Enter Expense ID: "))
    except ValueError:
        print("Please enter a valid Expense ID.")
        return

    for expense in expenses:
        if expense["id"] == expense_id:

            print("\nWhat do you want to update?")
            print("1. Amount")
            print("2. Category")
            print("3. Description")
            print("4. Payment Method")

            choice = input("Enter choice: ")

            if choice == "1":
                try:
                    new_amount = float(input("New amount: "))

                    if new_amount <= 0:
                        print("Amount must be greater than 0.")
                        return

                    expense["amount"] = new_amount

                except ValueError:
                    print("Please enter a valid amount.")
                    return

            elif choice == "2":
                new_category = input("New category: ").strip()

                if not new_category:
                    print("Category cannot be empty.")
                    return

                expense["category"] = new_category

            elif choice == "3":
                new_description = input("New description: ").strip()

                if not new_description:
                    print("Description cannot be empty.")
                    return

                expense["description"] = new_description

            elif choice == "4":
                new_payment_method = input("New payment method: ").strip()

                if not new_payment_method:
                    print("Payment method cannot be empty.")
                    return

                expense["payment_method"] = new_payment_method

            else:
                print("Invalid choice.")
                return

            print("Expense updated successfully!")
            return

    print("Expense ID not found.")


def delete_expense():
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses found.")
        return

    try:
        expense_id = int(input("Enter Expense ID: "))
    except ValueError:
        print("Please enter a valid Expense ID.")
        return

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            print("Expense deleted successfully!")
            return

    print("Expense ID not found.")


def search_expense():
    print("\n--- Search Expense ---")

    if not expenses:
        print("No expenses found.")
        return

    keyword = input("Search by category or description: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    found = False

    for expense in expenses:
        if (
            keyword in expense["category"].lower()
            or keyword in expense["description"].lower()
        ):
            print(
                f"ID: {expense['id']} | "
                f"₹{expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['description']} | "
                f"{expense['date']}"
            )

            found = True

    if not found:
        print("No matching expenses found.")


def expense_summary():
    print("\n--- Expense Summary ---")

    if not expenses:
        print("No expenses found.")
        return

    total = sum(expense["amount"] for expense in expenses)

    highest = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    lowest = min(
        expenses,
        key=lambda expense: expense["amount"]
    )

    average = total / len(expenses)

    print(f"Total Expenses    : ₹{total:.2f}")
    print(f"Number of Expenses: {len(expenses)}")
    print(f"Average Expense   : ₹{average:.2f}")

    print(
        f"Highest Expense   : ₹{highest['amount']:.2f} "
        f"({highest['description']})"
    )

    print(
        f"Lowest Expense    : ₹{lowest['amount']:.2f} "
        f"({lowest['description']})"
    )


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



main()
