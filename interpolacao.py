#!/usr/bin/env python3
"""Imprime a mensagem de um e-mail

NAO MANDE SPAM!!!
"""
__version__ = "0.2.0"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails.")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt

clientes = []
for line in open(filepath):
    # TODO: Substituir por list comprehension
    clientes.append(line.split(","))

# clientes = ["Maria", "João", "Bruno"]

for cliename, emailnte in clientes:
    # TODO: Substituir por envio de email
    print(f"Enviando email para {email}")
    print(
        open(templatepath).read()
        % { 
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "http//canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
print("-" * 50)