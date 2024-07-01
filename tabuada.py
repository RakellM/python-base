#!/usr/bin/env python
"""Imprime a badiaba do 1 ao 10.

Tabuada do 1
1
2
3
...
-------------
Tabuada do 2
2
4
6
...
-------------
"""
__version__ = "0.1.0"
__author__ = "Raquel Marques"

#numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1, 11)) #range do python é não inclusivo, se parar no 10 a lista vai só até o 9

# Iterable (percorríveis)

## para cada umero em numeros:
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-------------")