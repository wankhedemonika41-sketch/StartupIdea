# ================================
# U3 - OOP classes + Regex + Threading
# ================================

import re
import threading
import difflib


class IdeaProfile:
    """the class represents a startup idea with its title, description, and extracted keywords"""
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.keywords = []

    def set_keywords(self, keywords):
        self.keywords = keywords

    def __str__(self):
        return f"IdeaProfile(title={self.title}, keywords={self.keywords})"


class TrendMatcher:
    """The class is responsible for matching the extracted keywords with the trend data and calculating the viability score"""
    def __init__(self, trend_data):
        self.trend_data = trend_data

    def extract_with_regex(self, text):
        # by using rejex the letter/word pancution 
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        return words

    def find_matches(self, keywords):
        keyword_set = set(keywords)

        # Step 1 - Substring will match directly
        matches = {
            trend: score
            for trend, score in self.trend_data.items()
            if any(word in trend for word in keyword_set)
        }

        if matches:
            return matches

        # Step 2 - if direct match is not found then , similler will be found
        best_trends = {}
        for trend in self.trend_data:
            similarity = max(
                (difflib.SequenceMatcher(None, word, trend).ratio() for word in keyword_set),
                default=0
            )
            if similarity > 0.3:
                best_trends[trend] = similarity

        if best_trends:
            top_trends = sorted(best_trends.items(), key=lambda x: x[1], reverse=True)[:3]
            for trend, sim in top_trends:
                matches[trend] = round(self.trend_data[trend] * sim, 2)
            return matches

        # Step 3 - if nothing is found then show baseline generic score
        avg_score = round(sum(self.trend_data.values()) / len(self.trend_data) * 0.4, 2)
        matches = {"general market trend": avg_score}
        return matches


class ScoreEngine:
    """ the class which calculate Final viability score """
    def __init__(self, matches):
        self.matches = matches

    def calculate_score(self):
        if not self.matches:
            return 0
        avg_score = sum(self.matches.values()) / len(self.matches)
        return round(avg_score, 2)


# ---- Threading - to analyzed batch ----
def analyze_idea_thread(idea_text, trend_data, results, index):
    matcher = TrendMatcher(trend_data)
    keywords = matcher.extract_with_regex(idea_text)
    matches = matcher.find_matches(keywords)
    engine = ScoreEngine(matches)
    score = engine.calculate_score()
    results[index] = {"idea": idea_text, "score": score}


def batch_analyze(idea_list, trend_data):
    threads = []
    results = [None] * len(idea_list)

    for i, idea in enumerate(idea_list):
        t = threading.Thread(target=analyze_idea_thread, args=(idea, trend_data, results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # wait until the all thread are completed

    return results