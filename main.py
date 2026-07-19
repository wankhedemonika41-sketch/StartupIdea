from keyword_extractor import extract_keywords, sort_by_score, EmptyIdeaError
from models import IdeaProfile, TrendMatcher, ScoreEngine, batch_analyze
from db import save_idea, get_all_ideas

trend_data = {
    "food delivery": 85,
    "ai tool": 92,
    "fitness app": 70,
    "online education": 88,
    "budget travel": 65,
    "eco friendly": 80,
    "grocery delivery": 75,
    "mental health": 90,
    "remote work": 78,
    "gaming platform": 60,
    "fashion rental": 55,
    "pet care": 72,
    "elder care": 68,
    "crypto wallet": 50,
    "language learning": 83,
}


def match_trends(user_keywords):
    matches = {
        keyword: score
        for keyword, score in trend_data.items()
        if any(word in keyword for word in user_keywords)
    }
    return matches


if __name__ == "__main__":
    try:
        # Single idea analysis
        idea_text = input("Enter your startup idea: ")

        # U2 - keyword extraction + empty check
        keywords = extract_keywords(idea_text)
        print("Extracted keywords:", keywords)

        # U3 - regex based matcher + OOP classes
        matcher = TrendMatcher(trend_data)
        regex_keywords = matcher.extract_with_regex(idea_text)
        matches = matcher.find_matches(regex_keywords)

        engine = ScoreEngine(matches)
        print("Viability Score:", engine.calculate_score())

        # U2 - lambda sorting
        sorted_matches = sort_by_score(matches)
        print("Sorted matches:", sorted_matches)

        # U3 - threading batch test
        sample_ideas = ["food delivery app", "ai powered tool", "fitness tracking app"]
        batch_results = batch_analyze(sample_ideas, trend_data)
        print("Batch results:", batch_results)

    except EmptyIdeaError as e:
        print("Error:", e)

# U4 - save idea to MongoDB
final_score = engine.calculate_score()
saved_id = save_idea(idea_text, keywords, final_score)
print("Idea saved to MongoDB, ID:", saved_id)

# Show all saved ideas from MongoDB
print("\nAll saved ideas:")
for doc in get_all_ideas():
    print(doc)