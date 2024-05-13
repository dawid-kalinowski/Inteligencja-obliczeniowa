import text2emotion as te

positive_review = """
The room is new, nice, and modern. bed is super comfortable. The apartment is super clean and quiet.
New building. The heating is great. It is possible to rent the parking spot (which I recommend,
just 12 EUR + deposit for the pilot), this will save you much time.
"""

negative_review = """No bed, just a sofa (back folds flat, no mattress), dirty bedding, only 1 curtain for
2 windows so 1 window not covered, occasional noise from busy road, no free toiletries, communication
slow and only in polish"""

# Analyze emotions in positive review
positive_emotions = te.get_emotion(positive_review)

# Analyze emotions in negative review
negative_emotions = te.get_emotion(negative_review)

print("Emotions in Positive Review:", positive_emotions)
print("Emotions in Negative Review:", negative_emotions)