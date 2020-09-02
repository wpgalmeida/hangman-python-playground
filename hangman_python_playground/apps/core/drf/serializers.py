from rest_framework import serializers

from hangman_python_playground.apps.core.models import Categories, Player, Words, Game


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
