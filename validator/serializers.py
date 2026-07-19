from rest_framework import serializers


class IdeaInputSerializer(serializers.Serializer):
    idea_text = serializers.CharField(max_length=500)


class IdeaResultSerializer(serializers.Serializer):
    idea_text = serializers.CharField()
    score = serializers.FloatField()
    similar_startups = serializers.ListField()