from rest_framework import viewsets

from hangman_python_playground.apps.core.drf.serializers import (
    PlayerSerializer,
    CategoriesSerializer,
    WordsSerializer,
    GameSerializer,
    MoveSerializer,
)
from hangman_python_playground.apps.core.models import (
    Player,
    Categories,
    Words,
    Game,
    Move,
)


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class WordsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Words.objects.all()
    serializer_class = WordsSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class MoveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Move.objects.all()
    serializer_class = MoveSerializer
