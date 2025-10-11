#!/usr/bin/env python3
"""Calculator prefix

Mechanics:

[operation] [n1] [n2]

Operations:
sum -> +
sub -> -
mul -> *
div -> /

Use:
$ prefixcal.py sum 5 2
7

$ prefixcal.py mul 10 5
50

$ prefixcal.py
operation: sum
n1: 5
n2: 4
9
"""
__version__ = "0.3.1"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import os
import sys
from datetime import datetime

while True:

    arguments = sys.argv[1:]

    # Validation
    if not arguments:
        operation = input("operation:")
        n1 = input("n1:")
        n2 = input("n2:")
        arguments = [operation, n1, n2]
    elif len(arguments) != 3:
        print("Invalid number of arguments")
        print("ex: `sum 5 5")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ("sum", "sub", "mul", "div")
    if operation not in valid_operations:
        print("Invalid operation!")
        print(valid_operations)
        sys.exit(1)

    validated_nums = []
    for num in nums:
        # TODO: Repetition WHILE + exceptions
        if not num.replace(".", "").isdigit():
            print(f"Invalid number {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(f"{str(e)}")
        sys.exit(1)

    # TODO: Use functions dictionary
    if operation == "sum":
        result = n1 + n2
    elif operation == "sub":
        result = n1 - n2
    elif operation == "mul":
        result = n1 * n2
    elif operation == "div":
        result = n1 / n2

    path = os.curdir
    filepath = os.path.join(path, "prefixcal.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv('USER', 'anonymous')

    #print(f"{operation},{n1},{n2} = {result}", file=open(filepath, "a"))

    print(f"The result is {result}")

    try:
        with open(filepath, "a") as file_:
            file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")
    except PermissionError as e:
        # TODO: logging
        print(f"{str(e)}")
        sys.exit(1)
    
    if input("Press ENTER to continue or any other key to leave."):
        break



