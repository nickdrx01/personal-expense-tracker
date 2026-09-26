import re
from datetime import date


def extract_amount(text):
    match = re.search(r'\b\d+(?:\.\d+)?\b', text)

    if match:
        return float(match.group())

    return None


def extract_payment_method(text):
    text = text.lower()

    if "upi" in text:
        return "UPI"
    elif "cash" in text:
        return "Cash"
    elif "card" in text:
        return "Card"
    else:
        return "Unknown"


def suggest_category(description):

    description = description.lower()

    if any(word in description for word in
           ["food", "lunch", "dinner", "breakfast",
            "pizza", "snack", "tea"]):
        return "Food"

    elif any(word in description for word in
             ["bus", "train", "auto", "uber",
              "travel", "fuel"]):
        return "Travel"

    elif any(word in description for word in
             ["movie", "game", "netflix", "concert"]):
        return "Entertainment"

    elif any(word in description for word in
             ["shirt", "shoes", "clothes", "shopping"]):
        return "Shopping"

    elif any(word in description for word in
             ["course", "book", "college",
              "education", "udemy"]):
        return "Education"

    else:
        return "Other"


text = input("Enter your expense: ")

amount = extract_amount(text)
payment = extract_payment_method(text)
category = suggest_category(text)

print("\n===== EXPENSE DETAILS =====")
print("Amount:", amount)
print("Category:", category)
print("Description:", text)
print("Date:", date.today())
print("Payment Method:", payment)