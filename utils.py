def predict_category(description):

    keywords = {

        "Food": ["pizza", "burger", "restaurant", "food", "swiggy", "zomato"],
        "Travel": ["uber", "ola", "bus", "train", "flight", "taxi"],
        "Shopping": ["amazon", "flipkart", "mall", "clothes", "shopping"],
        "Entertainment": ["movie", "netflix", "game", "concert"],
        "Bills": ["electricity", "water", "internet", "rent"]
    }

    description = description.lower()

    for category, words in keywords.items():
        for word in words:
            if word in description:
                return category

    return "Other"