import uuid

from django.db import models

# Create your models here.
class StandardModelMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]


class Player(StandardModelMixin):
    name = models.CharField(max_length=100, blank=False)
    birth = models.DateField()
    gender = models.CharField(max_length=1, blank=False)  # Male, Female, Others


class Categories(StandardModelMixin):
    name_category = models.CharField(max_length=20, blank=False)


class Words(StandardModelMixin):
    word = models.CharField(max_length=20, blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)


class Game(StandardModelMixin):
    word = models.ForeignKey(Words, on_delete=models.CASCADE)
    end_game = models.BooleanField(default=False)


class Move(StandardModelMixin):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    letter = models.CharField(max_length=1, blank=False)
    right = models.BooleanField(default=False)
