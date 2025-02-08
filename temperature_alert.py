#!/usr/bin/env python3
"""
Temperature Alert

Create a script that asks the user the current temperature and the air 
humidity index and it will print the alert message depending on the conditions:

temp greater than 45: ALERT!!! Danger of extreme heat
temp times 3 greater or equal to humidity: ALERT!! Danger of humid heat
temp between 10 and 30: Normal
temp between 0 and 10: Cold
temp less 0: ALERT: Extreme cold

"""

__version__ = "0.1.0"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import os
import sys

arguments = sys.argv[1:]

if not arguments:
    temp = input("temperature in Celsius:")
    hum = input("humidity in %:")
    arguments = [temp, hum]
elif len(arguments) != 2:
    print("Invalid number of arguments")
    print("ex: `25 85")
    print("Temperature in Celsius | Humidity in percentage")
    sys.exit(1)

print(arguments)

temp, hum = arguments

validate_nums = []
for num in arguments:
    if not num.replace(".", "").isdigit():
        print(f"Invalid number {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validate_nums.append(num)

try:
    temp, hum = validate_nums
except ValueError as e:
    print(f"{str(e)}")
    sys.exit(1)

if temp >= 2 * hum and temp != 0 and hum != 0:
    print('ALERT!! Danger of humid heat')
else:
    if temp < 0:
        print('ALERT: Extreme cold')
    elif temp >= 0 and temp < 10:
        print('Cold')
    elif temp >= 10 and temp < 30:
        print('Normal')
    elif temp >= 10 and temp < 30:
        print('Normal')
    elif temp > 45:
        print('ALERT!!! Danger of extreme heat')
    else:
        print('I do not have a condition for that 🥴')

