"""Count words in each app review (in-code list) and print shortest, longest, and average.

Run from the repository root:
    python3 Week2/app_review_summary.py
Or from inside Week2:
    python3 app_review_summary.py
"""


def count_words(review):
    """Return the number of words in a review string."""
    return len(review.split())


def main():
    # Example list of app reviews (replace with your own reviews as needed).
    reviews = [
        "Really helpful app for tracking daily habits.",
        "Great design and easy to use, but notifications are inconsistent.",
        "I love the concept, though it crashes sometimes when I upload photos.",
        "Not bad.",
        "Fantastic experience overall. The onboarding was clear, features are useful, and the UI feels polished.",
    ]

    if not reviews:
        print("No reviews found.")
        return

    word_counts = [count_words(review) for review in reviews]

    print("Word count for each review:")
    for i, (review, count) in enumerate(zip(reviews, word_counts), start=1):
        print(f"  Review {i}: {count} words")

    shortest = min(word_counts)
    longest = max(word_counts)
    average = sum(word_counts) / len(word_counts)

    print("\nSummary:")
    print(f"  Shortest review: {shortest} words")
    print(f"  Longest review:  {longest} words")
    print(f"  Average review:  {average:.1f} words")


if __name__ == "__main__":
    main()
