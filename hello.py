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
__version__ = "0.1.3"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import os
import sys

print(f"{sys.argv}")
arguments = {
    "lang": None,
    "count": 1
}
for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: Logging
        print(f"[ERROR] {str(e)}")
        print("You need to use `=`")
        print(f"You passed {arg}")
        print("try with --key=value")
        sys.exit(1)
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
#    print(key, value)
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

"""
# Try with default value
message = msg.get(current_language, msg["en_US"])
"""

#EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(message * int(arguments["count"]))
