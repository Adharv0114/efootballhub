from rest_framework import serializers
from .models import Player, Squad, Comparison

# Player Serializer
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

# Squad Serializer
class SquadSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Squad
        fields = '__all__'

# Comparison Serializer
class ComparisonSerializer(serializers.ModelSerializer):
    player1 = PlayerSerializer()
    player2 = PlayerSerializer()

    class Meta:
        model = Comparison
        fields = '__all__'
