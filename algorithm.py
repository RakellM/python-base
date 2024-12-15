#!/usr/bin/env python3
"""PSEUDO CODE
Problem: Go to the grocery store and buy bread:
Premise: The grocery store open on weekends until 12pm, weekdays until 7pm, holidays (except Christmas) closed.

1. Is the grocery store open?
    1. if it is holiday AND it is NOT Christmas: NO
    2. else, if is is Saturday OR Sunday AND before 12pm: YES
    3. else, if it is weekday AND before 7pm: YES
    4. else: NO

2. If the grocery store is open AND:
    1. if it is raining: take umbrella
    2. if it is raining AND it is warm day: take umbrella and water bottle
    3. if it is raining AND it is a cold day OR it is snowing: take umbrella, jacket and boots
    4. Go to the grocery store:
        1. if they have whole grain bread AND Baguette: order 6 of each
        2. else, if they only have whole grain bread OR Baguette: order 12
        3. else: order 6 of any bread
3. Else:
    1. Stay at home and eat scones

"""

import go, take, order, have, eat, stay

# PREMISE
today = "Monday"
hour = 15
christmas = False
raining = True
cold_day = True
snowing = True
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
holiday = "Wednesday"
store_hours = {
    "weekday": 19,
    "weekend": 12
}

# Algorithm
if today in holiday and not christmas:
    store_open = False
elif today not in weekday and hour < store_hours["weekend"]:
    store_open = True
elif today in weekday and hour < store_hours["weekday"]:
    store_open = True
else:
    store_open = False

if store_open:
    if raining and (cold_day or snowing):
        take("umbrella")
        take("jacket")
        take("boots")
    elif raining and not cold_day:
        take("umbrella")
        take("water bottle")
    elif raining:
        take("umbrella")

    go("grocery")

    if have("whole grain bread") and have("baguette"):
        order(6, "whole grain bread")
        order(6, "baguette")
    elif have("whole grain bread") or have("baguette"):
        order(12, "each ")
    else:
        order(6, "any bread")
else:
    stay("home")
    eat("scone")