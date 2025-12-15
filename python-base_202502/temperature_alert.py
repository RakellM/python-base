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

__version__ = "0.1.3"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import sys
import logging

log = logging.Logger("temperature_alert")

# TODO: Move to utility module.


def is_completely_filled(dict_of_inputs):
    """Returns a boolean telling if a dict is completely filled."""
    info_size = len(dict_of_inputs)
    filled_size = len([value for value in dict_of_inputs.values() if value is not None])
    return info_size == filled_size


def read_inputs_for_dict(dict_of_info):
    """Reads information for a dict from user input."""
    for key in dict_of_info.keys():  # ["temperature", "humidity"]
        if dict_of_info[key] is not None:
            continue
        try:
            dict_of_info[key] = int(input(f"What is the {key}?").strip())
        except ValueError:
            log.error(f"Invalid {key}")
            break  # stop for
                         

## Main Code

info = { 
    "temperature": None ,
    "humidity": None
} 

while not is_completely_filled(info):
    read_inputs_for_dict(info)


temp, hum = info.values()   # unpacking

if temp > 45:
    print('ALERT!!! 🥵 Danger of extreme heat')
elif temp >= 30 and temp * 3 >= hum:
    print('ALERT!! 🥵♒ Danger of humid heat')
elif temp >= 10 and temp < 30:
    print('🙂 Normal')
elif temp >= 0 and temp < 10:
    print('🥶 Cold')
elif temp < 0:
    print('ALERT: ⛄ Extreme cold')

# TODO: humidity condition to be between 0 and 100
