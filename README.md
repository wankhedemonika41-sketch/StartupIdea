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

## Project Structure

```text
StartupIdea/
├── main.py                    # Standalone script for testing core logic
├── keyword_extractor.py       # Custom module - keyword extraction, exceptions, lambda sorting
├── models.py                  # IdeaProfile, TrendMatcher, ScoreEngine classes + threading
├── db.py                      # MongoDB connection + CRUD functions
├── config/                    # Django project settings
├── validator/                 # Django app
│   ├── views.py               # Form view + DRF API view
│   ├── serializers.py         # DRF serializers
│   └── templates/validator/   # HTML templates
├── manage.py
└── requirements.txt
```

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/wankhedemonika41-sketch/StartupIdea.git
cd StartupIdea
```

### 2. Create and activate a virtual environment
```bash
python -m venv myvenv
myvenv\Scripts\activate      # Windows
source myvenv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up MongoDB
Make sure MongoDB is running locally on `mongodb://localhost:27017/`. You can install [MongoDB Community Server](https://www.mongodb.com/try/download/community) and [MongoDB Compass](https://www.mongodb.com/products/compass) to view your data.

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Run the server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

---

## API Usage

**Endpoint:** `POST /api/analyze/`

**Body (form-data or x-www-form-urlencoded):**