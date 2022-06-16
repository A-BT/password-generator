# -*- coding: utf-8 -*-
# Python 3.10

# Functions
def generation_mode_control(mode):
    """
        This function checks if the generation mode is correct.

        Two modes are allowed :
            - shuffle mode (shuffle)
            - pattern mode (with allowed characters (A, a, 0, $)

        It controls if mode is "shuffle" mode or a correct pattern mode.

        If the control is OK, the function returns "1", else it returns "0".

        :param mode: str
            password generation mode to be checked : shuffle mode ("shuffle") or pattern mode (with "A" for upper,
            "a" for lower letter, "0" for number and "$" for special character

        :return: int
            the generation mode is allowed (1) or not (0)
        :return: str
            if control is not OK, it returns an error, else it returns ''
    """

    if mode != 'shuffle':
        pattern_chars_allowed = ['A', 'a', '0', '$']

        # [Check if the pattern is OK]
        for pattern_char in mode:
            if pattern_char not in pattern_chars_allowed:
                return 0, 'generation mode "' + str(mode) + '" is not allowed'

        return 1, ''

    return 1, ''


def variable_control(variable, variable_type):
    """
        This function checks if the registered variable have the good type and if integer is a positive number.

        If this control is OK, the function returns "1", else it returns "0".

        :param variable:
            variable to be checked
        :param variable_type:
            expected type

        :return: int
            type is OK (1) or not (0)
    """

    if type(variable) is not variable_type or (type(variable) is int and variable < 0):
        return 0
    return 1


def excluded_type_chars_control(type_chars):
    """
        This function checks if the excluded type of characters are correct.

        A correct excluded type of characters is "A" for upper, "a" for lower letter, "0" for number and "$" for special
        character.

        It's not possible to exclude all type of characters.

        :param type_chars: list
            the list with the excludes type of characters

        :return: int
            the excluded type of characters are allowed (1) or not (0)
        :return: str
            if control is not OK, it returns an error, else it returns ''
    """

    type_chars_allowed = ['A', 'a', '0', '$']

    # [Check if all type of characters are not excluded]
    if len(type_chars) ==4:
        return 0, 'All type of characters can\'t be excluded'

    # [Check if the excluded type of characters is OK]
    for type_char in type_chars:
        if type_char not in type_chars_allowed:
            return 0, 'Type chars excluded "' + str(type_char) + '" is not allowed'

    return 1, ''


def check_before_generation(generation_mode, length, repetition_allowed, min_upper_letters, min_lower_letters,
                            min_numbers, min_special_chars, excluded_chars, excluded_type_chars):
    """
        This function checks if everything is okay before the generation.

        It controls :
            - if the generation mode is OK
            - if variables type are OK
            - the password length (for shuffle mode) :
                - if it is higher than 0
                - if the length is not less than the sum of expected chars
            - if the list of excluded type of characters is correct (for shuffle mode)

        If the control is OK, the function returns "1", else it returns "0"

        :param generation_mode: str
            generation mode : shuffle mode or pattern mode
        :param length: int
            the length of the password, it must be positive
        :param repetition_allowed: int
            if repetition is allowed (1) or not (0)
        :param min_upper_letters: int
            minimum of upper letters in password
        :param min_lower_letters: int
            minimum of lower letters in password
        :param min_numbers: int
            minimum of numbers in password
        :param min_special_chars: int
            minimum of special chars in password
        :param excluded_chars: list
            list of excluded chars : excluded chars can't be used in the generated password
        :param excluded_type_chars: list
            list of "type of excluded chars" : to exclude a type of characters (example ['1', '$' to exclude numbers and
            special characters])

        :return: int
            the control is OK (1) or not (0)
        :return: str
            if control is not OK, it returns an error, else it returns ''
    """

    # [Check if generation mode is OK]
    is_correct_generation_mode, error_message = generation_mode_control(generation_mode)

    if is_correct_generation_mode == 0:
        return 0, error_message

    # [Pattern mode]
    if generation_mode != 'shuffle':
        # [Check if the type of variables type is OK]

        # list of tuples : (variable, type_expected)
        list_variables_type = [(repetition_allowed, int), (excluded_chars, list), (excluded_type_chars, list)]
        # length and minimum chars are not useful for pattern mode

        for each in list_variables_type:
            is_correct_variable = variable_control(each[0], each[1])

            if is_correct_variable == 0:

                if type(each[0]) is int and each[0] < 0:
                    error_message = 'integer must be a positive number'
                else:
                    error_message = 'variable "' + str(each[0]) + '" have a bad type. Expected type : ' + str(each[1])

                return 0, error_message

        return 1, ''

    else:  # [Shuffle mode]
        # [Check if the type of variables type is OK]

        # list of tuples : (variable, type_expected)
        list_variables_type = [(generation_mode, str), (length, int), (repetition_allowed, int),
                               (min_upper_letters, int), (min_lower_letters, int), (min_numbers, int),
                               (min_special_chars, int), (excluded_chars, list), (excluded_type_chars, list)]

        for each in list_variables_type:
            is_correct_variable = variable_control(each[0], each[1])

            if is_correct_variable == 0:

                if type(each[0]) is int and each[0] < 0:
                    error_message = 'integer must be a positive number'
                else:
                    error_message = 'variable "' + str(each[0]) + '" have a bad type. Expected type : ' + str(each[1])

                return 0, error_message

        # [Check if the password length is correct]
        if length < 1:
            return 0, 'the password length can\'t be less than 1 character'

        # [Check if the sum of minimum characters is lower or equal to the password length]
        if length < (min_upper_letters + min_lower_letters + min_numbers + min_special_chars):
            return 0, 'the password length is lower than the sums of minimum characters'

        # [Check if excluded type of characters is OK]
        if excluded_type_chars != ['']:
            is_correct_excluded_type_chars, error_message = excluded_type_chars_control(excluded_type_chars)
        else:
            is_correct_excluded_type_chars = 1

        if is_correct_excluded_type_chars == 0:
            return 0, error_message

        return 1, ''
