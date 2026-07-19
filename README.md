# StartupIdea Validator

A Startup Idea Validator that extracts keywords from a raw idea description, matches it against market trends, and generates a viability score along with a "how to start" checklist — without requiring perfectly structured input.

---

## Project Overview

| Category | Details |
|---|---|
| **Project Name** | StartupIdea |
| **Domain** | Productivity |
| **Type** | Full-stack Web Application + REST API |
| **Status** | ✅ Complete |

StartupIdea understands raw text like *"AI powered fitness app for students"* or *"pizza shop"* and converts it into a structured **viability score**, matched market trends, and a clear list of what's needed to actually start the business.

---

## Features

- Upload your startup idea via a simple web form
- Keyword extraction from idea text (regex based)
- Market trend matching against a curated trend database
- Fuzzy matching fallback — finds the closest trend even if no exact match is found
- Viability score (0–100) with a verdict: Strong Potential / Worth Exploring / Needs Rework
- "How to start" checklist tailored to the matched startup category
- Every submitted idea saved to MongoDB
- REST API endpoint for programmatic access

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| API | Django REST Framework |
| Database | MongoDB (via pymongo) |
| Core Logic | Sets, Dicts, Comprehensions, OOP, Regex, Threading |
| Frontend | Django templates + custom CSS |

---

## Project Structure

StartupIdea/
├── main.py                  # Standalone script for testing
├── keyword_extractor.py     # Custom module - keyword
├── models.py                # IdeaProfile, TrendMatcher etc
├── db.py                    # MongoDB connection + CRUD opr
├── config/                  # Django project settings
├── validator/               # Django app
│   ├── views.py             # Form view + DRF API view
│   ├── serializers.py       # DRF serializers
│   └── templates/validator/ # HTML templates
├── manage.py
└── requirements.txt