def suggest_category(description):

    description = description.lower()

    if any(word in description for word in
           ["food", "lunch", "dinner", "breakfast", "pizza", "snack", "tea"]):
        return "Food"

    elif any(word in description for word in
             ["bus", "train", "auto", "uber", "travel", "fuel"]):
        return "Travel"

    elif any(word in description for word in
             ["movie", "game", "netflix", "concert"]):
        return "Entertainment"

    elif any(word in description for word in
             ["shirt", "shoes", "clothes", "shopping"]):
        return "Shopping"

    elif any(word in description for word in
             ["course", "book", "college", "education", "udemy"]):
        return "Education"

    else:
        return "Other"


description = input("Enter expense description: ")

category = suggest_category(description)

print("\nSuggested category:", category)