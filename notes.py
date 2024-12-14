#!/usr/bin/env python3
"""Notepad

$ notes.py new "My Note"
tag: tech
text: 
General note about a career in technology.

$ notes.py read --tag=tech
...
...

"""
__version__ = "0.1.0"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify a subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    # read notes
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    # create a new note
    title = arguments[1]  # TODO: deal with exception
    text = [
        f"{title}" ,
        input("tag:").strip() ,
        input("text:\n").strip() ,
    ]
    # \t - tsv
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

