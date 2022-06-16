# -*- coding: utf-8 -*-
# Python 3.10

# Imports

# Import personal modules
from password_generator import password_generation

is_generated, error, password = password_generation(5, 'shuffle', 1, 0, 0, 0, 0, ['$'], ['1'])
if is_generated == 1:
    print(password)
else:
    print('Generation error : ' + error)
