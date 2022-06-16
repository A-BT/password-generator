# -*- coding: utf-8 -*-
# Python 3.10

# Imports

# Import default modules
import string
from secrets import choice  # Choose one of them
# from random import choice  # Choose one of them

# Import personal modules
from controls import check_before_generation


# Functions

def exclude_chars(list_chars, list_excluded_chars):
    """
        This function excludes the given characters from a list of characters.
        It takes a list of characters and returns this list less the excluded characters.
        :param list_chars: list
            the list before excluding characters
        :param list_excluded_chars: list
            the list of excluded characters
        :return list_chars: list
            the list less the excluded characters
    """

    for char in list_excluded_chars:
        if char in list_chars:
            list_chars.remove(char)

    return list_chars


def generate_lists_chars(mode, min_upper, min_lower, min_nb, min_spec, list_excluded_chars):
    """
        This function generates 4 lists :
            - list of upper letters
            - list of lower letters
            - list of numbers
            - list of special characters

        Lists are generated without excluded characters.

        :param mode: str
            generation mode : shuffle mode or pattern mode
        :param min_upper:int
            the minimum number of upper letters expected in the password
        :param min_lower:int
            the minimum number of lower letters expected in the password
        :param min_nb:int
            the minimum number of numbers expected in the password
        :param min_spec:int
            the minimum number of special characters expected in the password
        :param list_excluded_chars: list
            list of excluded characters

        :return list_upper_letters: list
            list of upper letters
        :return list_lower_letters: list
            list of lower letters
        :return list_numbers: list
            list of numbers
        :return list_special_chars: list
            list of special chars
    """

    if mode != 'shuffle' or (mode == 'shuffle' and min_upper > 0):
        list_upper_letters = list(string.ascii_uppercase)
        list_upper_letters = exclude_chars(list_upper_letters, list_excluded_chars)
    else:
        list_upper_letters = []

    if mode != 'shuffle' or (mode == 'shuffle' and min_lower > 0):
        list_lower_letters = list(string.ascii_lowercase)
        list_lower_letters = exclude_chars(list_lower_letters, list_excluded_chars)
    else:
        list_lower_letters = []

    if mode != 'shuffle' or (mode == 'shuffle' and min_nb > 0):
        list_numbers = list(string.digits)
        list_numbers = exclude_chars(list_numbers, list_excluded_chars)
    else:
        list_numbers = []

    if mode != 'shuffle' or (mode == 'shuffle' and min_spec > 0):
        list_special_chars = list(string.punctuation)
        list_special_chars = exclude_chars(list_special_chars, list_excluded_chars)
    else:
        list_special_chars = []

    return list_upper_letters, list_lower_letters, list_numbers, list_special_chars


def draw_random(list_chars, passwd, repetition):
    """
        This function returns a random character draw in a list.

        It returns a character after a control if repetition is allowed or not.

        :param list_chars:list
            list of characters in which the function will draw
        :param passwd: str
            the start of generated password
        :param repetition: int
            repetition is allowed (1) or not (0)

        :return: str
            randomly drawn character
    """

    char = choice(list_chars)

    if repetition == 0:
        while char == passwd[-1:]:
            char = choice(list_chars)
    else:
        char = choice(list_chars)

    return char


def password_generation(generation_mode, length=1, repetition_allowed=1, min_upper_letters=0, min_lower_letters=0,
                        min_numbers=0, min_special_chars=0, excluded_chars=None, excluded_type_chars=None):

    if excluded_chars is None:
        excluded_chars = ['']
    if excluded_type_chars is None:
        excluded_type_chars = ['']

    # [Check before generation]
    check_is_ok, error_msg = check_before_generation(generation_mode, length, repetition_allowed, min_upper_letters,
                                                     min_lower_letters, min_numbers, min_special_chars, excluded_chars,
                                                     excluded_type_chars)

    if check_is_ok == 0:
        return check_is_ok, error_msg, ''

    # [Generation]

    # [Pattern mode]
    if generation_mode != 'shuffle':
        password = ''

        # Generate lists of upper and lower letters, list of numbers and list of special chars
        list_upper, list_lower, list_nb, list_spec = generate_lists_chars(generation_mode, min_upper_letters,
                                                                          min_lower_letters, min_numbers,
                                                                          min_special_chars, excluded_chars)

        for pattern_char in generation_mode:
            if pattern_char == 'A':
                new_char = draw_random(list_upper, password, repetition_allowed)
                password += new_char

            if pattern_char == 'a':
                new_char = draw_random(list_lower, password, repetition_allowed)
                password += new_char

            if pattern_char == '0':
                new_char = draw_random(list_nb, password, repetition_allowed)
                password += new_char

            if pattern_char == '$':
                new_char = draw_random(list_spec, password, repetition_allowed)
                password += new_char


        return 1, '', password









    password = 'passwd'

    return 1, '', password
