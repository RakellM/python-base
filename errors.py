#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to Ask Forgiveness than Permission

try:
    names = open("names.txt").readlines() # FileNotFoundError
    1 / 1 # ZeroDivisionError
    print(names.append) # AttributeError
except FileNotFoundError:
    print("[Error] File names.txt not found!")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You cannnot divide by zero!")
    sys.exit(1)
except AttributeError:
    print("[Error] List does not have banana.")
    sys.exit(1)


try:
    print(names[2])
except:
    print("[Error] Missing name in the list.")
    sys.exit(1)
