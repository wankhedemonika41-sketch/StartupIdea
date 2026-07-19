# ================================
# U4 - MongoDB Connection + CRUD
# ================================

from pymongo import MongoClient

# Local MongoDB sobat connect
client = MongoClient("mongodb://localhost:27017/")

db = client["startupidea"]
ideas_collection = db["user_ideas"]


def save_idea(idea_text, keywords, score):
    """CREATE - navin idea save kar"""
    idea_doc = {
        "idea_text": idea_text,
        "keywords": keywords,
        "score": score,
    }
    result = ideas_collection.insert_one(idea_doc)
    return result.inserted_id


def get_all_ideas():
    """READ - sagLya ideas fetch kar"""
    ideas = list(ideas_collection.find())
    return ideas


def update_idea_score(idea_id, new_score):
    """UPDATE - existing idea cha score update kar"""
    ideas_collection.update_one(
        {"_id": idea_id},
        {"$set": {"score": new_score}}
    )


def delete_idea(idea_id):
    """DELETE - idea remove kar"""
    ideas_collection.delete_one({"_id": idea_id})