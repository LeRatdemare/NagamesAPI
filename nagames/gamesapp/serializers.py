from gamesapp.models import *
from rest_framework import serializers

class GameSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSession
        fields = ('title', 'admin', 'official_homepage')