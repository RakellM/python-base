#!/usr/bin/env python3
"""Hello World Multi Languages.

Depending on the configured language in the environment the code will shown 
the mesaage accordingly.

How to:

Have a LANG variable configured eg.

    export LANG=pt_BR

Execution:

    python3 hello.py
    or
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en-US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])
