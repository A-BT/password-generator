# -*- coding: utf-8 -*-
# Python 3.10

# Imports

# Import default modules

# Functions
def password_generation(length, generation_mode, repetition_allowed, min_upper_letters, min_lower_letters, min_numbers,
                        min_special_chars, excluded_chars=None, excluded_type_chars=None):

    if excluded_chars is None:
        excluded_chars = ['']
    if excluded_type_chars is None:
        excluded_type_chars = ['']

    password = ''

    return 1, '', password
