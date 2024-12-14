#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to Ask Forgiveness than Permission

try:
    names = open("names.txt").readlines() 
    # FileNotFoundError
except FileNotFoundError as e:
    print("{str(e)}")
    sys.exit(1)
    # TODO: Use retry
else:
    print("Success!")
finally:
    print("Always run this text!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list.")
    sys.exit(1)
