#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to Ask Forgiveness than Permission

try:
    names = open("names.txt").readlines()
except: # Bare except
    print("[Error] File names.txt not found!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list.")
    sys.exit(1)
