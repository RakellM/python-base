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
__version__ = "0.3.2"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import os
import sys
from datetime import datetime

arguments = sys.argv[1:]

valid_operations = {
    "sum": lambda a, b: a + b, 
    "sub": lambda a, b: a - b, 
    "mul": lambda a, b: a * b, 
    "div": lambda a, b: a / b,
}

path = os.curdir
filepath = os.path.join(path, "prefixcal.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')



while True:
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

    result = valid_operations[operation](n1, n2)

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



