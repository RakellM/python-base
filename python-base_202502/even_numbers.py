#!/usr/bin/env python3
"""
Create a script that show on the screen all the even numbers from 1 to 200.

example:
`python3 even_numbers.py`
2
4
6
8
...

"""

__version__ = "0.1.1"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

array_nbrs = range (1, 201)

for nbr in array_nbrs:
    if nbr % 2 != 0:
        continue
    print(nbr)

