# Customer Feedback Analysis

def positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available."
    positive = [r for r in ratings if r >= 4]
    percentage = (len(positive) / len(ratings)) * 100
    return round(percentage, 2)


if __name__ == "__main__":
    ratings = [5, 4, 3, 5, 2, 4, 1, 5]
    result = positive_feedback_percentage(ratings)
    print(f"Positive Feedback: {result}%")
