#!/usr/bin/env python3
"""
Repeat Vowel

Create a script that asks the user to type one or more words and
print each word with their vowels duplicated.

example:
python repeat_vowel.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Raquel
'Digite uma palavra (ou enter para sair):' P<enter>
Pythoon
Raaquueel

"""

__version__ = "0.1.0"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import sys
import logging

log = logging.Logger("repeat_vowel")

inputs_list = []
output_list = []

vowels = "aeiou"

while True:
    word = input("Digite uma palavra (ou enter para sair):").strip()
    final_word = ''
    for letter in word:
        # TODO: Remove accents with a fucntion.
        if letter.lower() in vowels:
            final_word += letter *2
        else:
            final_word += letter
    output_list.append(final_word)
    if not word:
        break
    inputs_list.append(word)

print(inputs_list)

for word in output_list:
    print(word)

