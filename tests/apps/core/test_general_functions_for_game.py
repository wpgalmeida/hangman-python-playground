from datetime import datetime

from django.test import TestCase

from hangman_python_playground.apps.core.general_functions_for_game import (
    get_word,
    get_positions_of_letter_in_word,
    check_end_game,
)
from hangman_python_playground.apps.core.models import Categories, Words


class Test(TestCase):
    def setUp(self) -> None:
        self.name_category = "Animais"

        self.category = Categories.objects.create(name_category=self.name_category)

        Words.objects.create(word="Girafa", category=self.category)
        Words.objects.create(word="Camelo", category=self.category)
        Words.objects.create(word="Guepardo", category=self.category)
        Words.objects.create(word="Marsupial", category=self.category)
        Words.objects.create(word="Hipopótamo", category=self.category)

    def test_should_return_a_word_given_a_category(self):
        expected_count_value = 1
        word = get_word(self.category)
        qs_word = Words.objects.filter(word=word)

        self.assertEqual(qs_word.count(), expected_count_value)

    def test_should_return_list_with_positions(self):
        expected_list = [1, 3, 5]
        list = get_positions_of_letter_in_word("a", "banana")

        self.assertEqual(expected_list, list)

    def test_should_end_game_for_win(self):
        num_errors = 5
        right_letters = ["C", "a", "m", "e", "l", "o"]

        end_game = check_end_game(num_errors, right_letters)

        self.assertTrue(end_game)

    def test_should_end_game_for_loss(self):
        num_errors = 6
        right_letters = ["_", "a", "m", "e", "l", "o"]

        end_game = check_end_game(num_errors, right_letters)

        self.assertTrue(end_game)

    def test_should_not_end_game(self):
        num_errors = 5
        right_letters = ["_", "a", "m", "e", "l", "o"]

        end_game = check_end_game(num_errors, right_letters)

        self.assertFalse(end_game)
