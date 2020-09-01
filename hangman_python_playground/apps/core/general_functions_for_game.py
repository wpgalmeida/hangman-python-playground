from random import randrange

from hangman_python_playground.apps.core.models import Words


class DontExistsWordForThatCategory(Exception):
    pass


def get_word(category):
    word = ""
    qs_words = Words.objects.filter(category=category)
    size = qs_words.count()

    if size < 1:
        raise DontExistsWordForThatCategory()
    else:
        rand_ind = randrange(size)
        word = qs_words[rand_ind].word

    return word


def get_positions_of_letter_in_word(inp_letter, inp_word):
    position = 0
    list_positions = []

    for letter in inp_word:
        if inp_letter.upper() == letter.upper():
            list_positions.append(position)
        position += 1

    return list_positions


def check_end_game(num_of_errors, right_letters):
    if num_of_errors == 6:
        return True
    elif "_" not in right_letters:
        return True

    return False
