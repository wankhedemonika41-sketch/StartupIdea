from django.contrib import admin
from django.urls import path
from validator.views import analyze_idea, analyze_idea_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', analyze_idea, name='analyze_idea'),
    path('api/analyze/', analyze_idea_api, name='analyze_idea_api'),
]