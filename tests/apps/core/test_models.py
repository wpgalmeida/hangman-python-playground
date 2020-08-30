from datetime import datetime

from django.db import IntegrityError
from django.test import TestCase

from hangman_python_playground.apps.core.models import (
    Player,
    Categories,
    Words,
    Game,
    Move,
)


class Test(TestCase):
    def setUp(self) -> None:
        self.name = "Augusto Carrara"
        str_birth = "2020-01-01"
        self.birth = datetime.strptime(str_birth, "%Y-%m-%d").date()
        self.gender = "M"

        self.name_category = "Animais"
        self.word = "Girafa"

    # tests for player
    def test_should_create_player(self):
        expected_count_value = 1
        player = Player.objects.create(
            name=self.name, birth=self.birth, gender=self.gender
        )

        self.assertEqual(Player.objects.all().count(), expected_count_value)
        self.assertEqual(player.name, self.name)
        self.assertEqual(player.birth, self.birth)
        self.assertEqual(player.gender, self.gender)

    def test_should_not_null_constraint_given_player_without_name(self):
        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_player.name"
        ):
            Player.objects.create(name=None, birth=self.birth, gender=self.gender)

    def test_should_not_null_constraint_given_player_without_gender(self):
        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_player.gender"
        ):
            Player.objects.create(name=self.name, birth=self.birth, gender=None)

    def test_should_not_null_constraint_given_player_without_birth(self):
        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_player.birth"
        ):
            Player.objects.create(name=self.name, gender=None)

    # Test for Categories
    def test_should_create_categories(self):
        expected_count_value = 1
        category = Categories.objects.create(name_category=self.name_category)

        self.assertEqual(Categories.objects.all().count(), expected_count_value)
        self.assertEqual(category.name_category, self.name_category)

    def test_should_not_null_constraint_given_category_without_name_category(self):
        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_categories.name_category"
        ):
            Categories.objects.create(name_category=None)

    # Test for Words
    def test_should_create_words(self):
        expected_count_value = 1
        category_created = Categories.objects.create(name_category=self.name_category)
        word_created = Words.objects.create(word=self.word, category=category_created)

        self.assertEqual(Words.objects.all().count(), expected_count_value)
        self.assertEqual(word_created.word, self.word)

    def test_should_not_null_constraint_given_worlds_without_word(self):
        category_created = Categories.objects.create(name_category=self.name_category)

        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_words.word"
        ):
            Words.objects.create(word=None, category=category_created)

    def test_should_not_null_constraint_given_worlds_without_category(self):
        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_words.category_id"
        ):
            Words.objects.create(word=self.word)

    # Tests for Game
    def test_should_create_game(self):
        expected_count_value = 1
        category_created = Categories.objects.create(name_category=self.name_category)
        word_created = Words.objects.create(word=self.word, category=category_created)
        game_created = Game.objects.create(word=word_created)

        self.assertEqual(Game.objects.all().count(), expected_count_value)
        self.assertEqual(game_created.word, word_created)
        self.assertFalse(game_created.end_game)

    def test_should_update_end_game_in_game(self):
        expected_count_value = 1
        category_created = Categories.objects.create(name_category=self.name_category)
        word_created = Words.objects.create(word=self.word, category=category_created)
        game_created = Game.objects.create(word=word_created)

        self.assertEqual(Game.objects.all().count(), expected_count_value)
        self.assertEqual(game_created.word, word_created)
        self.assertFalse(game_created.end_game)

        Game.objects.filter(id=game_created.id).update(end_game=True)

        game_update = Game.objects.all().first()

        self.assertTrue(game_update.end_game)

    def test_should_not_null_constraint_given_game_without_word(self):
        category_created = Categories.objects.create(name_category=self.name_category)
        word_created = Words.objects.create(word=self.word, category=category_created)
        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_game.word_id"
        ):
            Game.objects.create()

    # Tests for Move
    def test_should_create_move(self):
        expected_count_value = 1
        player_created = Player.objects.create(
            name=self.name, birth=self.birth, gender=self.gender
        )
        category_created = Categories.objects.create(name_category=self.name_category)
        word_created = Words.objects.create(word=self.word, category=category_created)
        game_created = Game.objects.create(word=word_created)
        move_created = Move.objects.create(
            player=player_created, game=game_created, letter="a"
        )

        self.assertEqual(Move.objects.all().count(), expected_count_value)
        self.assertEqual(move_created.player, player_created)
        self.assertEqual(move_created.game, game_created)
        self.assertEqual(move_created.letter, "a")
        self.assertFalse(move_created.right)

    def test_should_not_null_constraint_give_move_without_letter(self):
        player_created = Player.objects.create(
            name=self.name, birth=self.birth, gender=self.gender
        )
        category_created = Categories.objects.create(name_category=self.name_category)
        word_created = Words.objects.create(word=self.word, category=category_created)
        game_created = Game.objects.create(word=word_created)

        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_move.letter"
        ):
            Move.objects.create(player=player_created, game=game_created, letter=None)

    def test_should_not_null_constraint_give_move_without_player(self):
        category_created = Categories.objects.create(name_category=self.name_category)
        word_created = Words.objects.create(word=self.word, category=category_created)
        game_created = Game.objects.create(word=word_created)

        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_move.player"
        ):
            Move.objects.create(game=game_created, letter="a")

    def test_should_not_null_constraint_give_move_without_game(self):
        player_created = Player.objects.create(
            name=self.name, birth=self.birth, gender=self.gender
        )
        category_created = Categories.objects.create(name_category=self.name_category)
        word_created = Words.objects.create(word=self.word, category=category_created)

        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_move.game"
        ):
            Move.objects.create(player=player_created, letter="a")
