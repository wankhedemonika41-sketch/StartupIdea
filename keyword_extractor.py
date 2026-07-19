# ================================
# U2 - Custom Module + Exception + Lambda
# ================================

# Custom exception - if user input is empty, raise this exception
class EmptyIdeaError(Exception):
    pass


# Common words which are not useful for keyword extraction
STOPWORDS = {"a", "an", "the", "for", "and", "or", "to", "of", "in", "on", "is", "with"}


def extract_keywords(idea_text):
    if not idea_text or idea_text.strip() == "":
        raise EmptyIdeaError("Idea text is empty. Please provide a valid startup idea.")

    words = idea_text.lower().split()
    keywords = [word for word in words if word not in STOPWORDS]
    return keywords


def sort_by_score(matches_dict):
    # Lambda function to sort the matches dictionary by score in descending order
    sorted_items = sorted(matches_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_items