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

    password = 'passwd'

    return 1, '', password
