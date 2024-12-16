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
__version__ = "0.1.1"
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
    try:
        arg_tag = arguments[1].lower()
    except IndexError:
        arg_tag = input("What is the tag:").strip().lower()
    
    # read notes
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arg_tag:
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    try:
        title = arguments[1]
    except IndexError:
        title = input("What is the title:").strip().title()

    # create a new note
    text = [
        f"{title}" ,
        input("tag:").strip() ,
        input("text:\n").strip() ,
    ]
    # \t - tsv
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

