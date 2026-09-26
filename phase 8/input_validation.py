def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("❌ Please enter a valid number.")


def get_category():
    while True:
        category = input("Enter category: ").strip()

        if category == "":
            print("❌ Category cannot be empty.")
            continue

        return category


def get_payment_method():
    allowed_methods = ["UPI", "Cash", "Card"]

    while True:
        payment = input("Enter payment method: ").strip().title()

        if payment in allowed_methods:
            return payment

        print("❌ Invalid payment method.")
        print("Allowed:", ", ".join(allowed_methods))


print("\n===== INPUT VALIDATION TEST =====")

amount = get_amount()
category = get_category()
payment = get_payment_method()

print("\n===== VALID DATA =====")
print("Amount:", amount)
print("Category:", category)
print("Payment Method:", payment)