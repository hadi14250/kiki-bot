from difflib import SequenceMatcher

def get_similarity_percentage(sentence1, sentence2):
    # Create a SequenceMatcher object
    seq_matcher = SequenceMatcher(None, sentence1, sentence2)

    # Get the ratio of similarity (a float between 0 and 1)
    similarity_ratio = seq_matcher.ratio()

    # Convert the similarity ratio to a percentage
    similarity_percentage = similarity_ratio * 100

    return similarity_percentage

# Example usage
sentence1 = 'Koimoi.com on Instagram: "u0040saratendulkar pours her heart into a birthday wish for her world, her Mom u0040tendulkaranjali u2764ufe0fud83eudef6 #saratendulkar #anjalitendulkar #koimoi Sara Tendulkar, Anjali Tendulkar, Birthday Wish, Mother Daughter'
sentence2 = 'u0040saratendulkar pours her heart into a birthday wish for her world, her Mom u0040tendulkaranjali u2764ufe0fud83eudef6 #saratendulkar #anjalitendulkar #koimoi Sara Tendulkar, Anjali Tendulkar, Birthday Wish, Mother Daughter'
percentage = get_similarity_percentage(sentence1, sentence2)

print(f"Similarity Percentage: {percentage}%")