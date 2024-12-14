#!/usr/bin/env python3

import os
import sys

# LBYL - Look before You Leap

if os.path.exists("names.txt"):
    print("The file exists.")
    input("...") # Race Condition
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found!")

if len(names) >= 4:
    print(names[2])
else:
    print("[Error] Missing name in the list.")
    sys.exit(1)
