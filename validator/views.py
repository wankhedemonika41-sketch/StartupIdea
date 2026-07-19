import re
import threading
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Apla U1-U4 cha logic import kar
from keyword_extractor import extract_keywords, sort_by_score, EmptyIdeaError
from models import TrendMatcher, ScoreEngine
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
    "beauty parlour": 74,
}

startup_requirements = {
    "food delivery": ["Kitchen/cloud kitchen space", "Delivery partners ani vehicles", "FSSAI food license", "Packaging supplies", "Delivery app/website"],
    "ai tool": ["Skilled developers/ML engineers", "Cloud server (AWS/GCP)", "Dataset access", "SaaS subscription model", "Beta testers"],
    "fitness app": ["App developers", "Certified fitness trainers content", "Server/hosting", "Payment gateway integration", "Marketing budget"],
    "online education": ["Subject matter experts/teachers", "Video recording setup", "LMS platform", "Content library", "Digital marketing"],
    "budget travel": ["Travel agency license", "Local vendor tie-ups (hotels/transport)", "Website/booking system", "Customer support team", "Insurance partnerships"],
    "eco friendly": ["Sustainable raw material sourcing", "Manufacturing/production unit", "Eco certification", "Distribution network", "Brand storytelling/marketing"],
    "grocery delivery": ["Warehouse/storage space", "Supplier tie-ups", "Delivery fleet", "Inventory management system", "FSSAI license"],
    "mental health": ["Licensed therapists/counselors", "Confidential platform (video/chat)", "Data privacy compliance", "Insurance/payment setup", "Awareness marketing"],
    "remote work": ["Collaboration software", "Cloud infrastructure", "HR/payroll tools", "Cybersecurity setup", "Client acquisition strategy"],
    "gaming platform": ["Game developers/designers", "Servers for hosting", "Gaming license (if betting involved)", "Community management", "Monetization strategy (ads/IAP)"],
    "fashion rental": ["Physical store or warehouse", "Inventory of clothing/accessories", "Cleaning/dry-cleaning tie-up", "Delivery/logistics", "Website/app for booking"],
    "pet care": ["Shop/clinic space", "Licensed veterinarian (if medical)", "Pet supplies inventory", "Trained staff", "Local advertising"],
    "elder care": ["Trained caregiving staff", "Medical tie-ups/nurses", "Home visit logistics or facility space", "Licenses for healthcare services", "Trust-building marketing"],
    "crypto wallet": ["Blockchain developers", "Security audits", "Regulatory/legal compliance", "Server infrastructure", "User trust & KYC system"],
    "language learning": ["Language experts/tutors", "App/website platform", "Course content creation", "Payment gateway", "Community/practice features"],
    "beauty parlour": ["Shop space/location (good footfall area)", "Trained beauticians/staff", "Equipment ani cosmetic supplies", "Shop license/registration", "Local marketing ani word of mouth"],
}

default_requirements = [
    "Business registration/license",
    "Initial investment/funding",
    "A physical or online location/setup",
    "Team hiring",
    "Marketing to reach first customers",
]


def get_requirements(sorted_matches):
    for trend_name, _ in sorted_matches:
        if trend_name in startup_requirements:
            return startup_requirements[trend_name]
    return default_requirements


def get_verdict(score):
    if score >= 75:
        return "Strong Potential", "verdict-strong"
    elif score >= 45:
        return "Worth Exploring", "verdict-medium"
    else:
        return "Needs Rework", "verdict-low"


def analyze_idea(request):
    context = {}

    if request.method == "POST":
        idea_text = request.POST.get("idea_text", "")

        try:
            keywords = extract_keywords(idea_text)

            matcher = TrendMatcher(trend_data)
            regex_keywords = matcher.extract_with_regex(idea_text)
            matches = matcher.find_matches(regex_keywords)

            engine = ScoreEngine(matches)
            score = engine.calculate_score()

            sorted_matches = sort_by_score(matches)
            requirements = get_requirements(sorted_matches)
            verdict, verdict_class = get_verdict(score)

            # MongoDB madhe save kar
            save_idea(idea_text, keywords, score)

            context["idea_text"] = idea_text
            context["score"] = score
            context["similar_startups"] = sorted_matches
            context["keywords"] = keywords
            context["requirements"] = requirements
            context["verdict"] = verdict
            context["verdict_class"] = verdict_class
            context["success"] = True

        except EmptyIdeaError as e:
            context["error"] = str(e)

    return render(request, "validator/index.html", context)


@api_view(['POST'])
def analyze_idea_api(request):
    idea_text = request.data.get("idea_text", "")

    try:
        keywords = extract_keywords(idea_text)

        matcher = TrendMatcher(trend_data)
        regex_keywords = matcher.extract_with_regex(idea_text)
        matches = matcher.find_matches(regex_keywords)

        engine = ScoreEngine(matches)
        score = engine.calculate_score()

        sorted_matches = sort_by_score(matches)
        requirements = get_requirements(sorted_matches)

        save_idea(idea_text, keywords, score)

        return Response({
            "idea_text": idea_text,
            "score": score,
            "similar_startups": sorted_matches,
            "requirements": requirements,
        }, status=200)

    except EmptyIdeaError as e:
        return Response({"error": str(e)}, status=400)