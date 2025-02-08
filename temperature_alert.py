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

__version__ = "0.1.1"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import sys
import logging

log = logging.Logger("temperature_alert")

info = { 
    "temperature": None ,
    "humidity": None
} 

keys = info.keys()

for key in keys: 
    try:
        info[key] = float(input(f"What is the {key}?").strip())
    except ValueError:
        log.error(f"Invalid {key}")
        sys.exit(1)

temp = info['temperature']
hum = info["humidity"]

if temp > 45:
    print('ALERT!!! 🥵 Danger of extreme heat')
elif temp * 3 >= hum and temp != 0:
    print('ALERT!! 🥵♒ Danger of humid heat')
elif temp >= 10 and temp < 30:
    print('🙂 Normal')
elif temp >= 0 and temp < 10:
    print('🥶 Cold')
elif temp < 0:
    print('ALERT: ⛄ Extreme cold')
