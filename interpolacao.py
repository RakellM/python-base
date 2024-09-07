#!/usr/bin/env python3
"""Imprime a mensagem de um e-mail

NAO MANDE SPAM!!!
"""
__version__ = "0.1.0"
__author__ = "Raquel Marques"
__license__ = "Unlicense"

email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Clique agora em %(link)s

Apenas %(quantidade)d disponíveis!

Preço promocional %(preco).2f
"""

clientes = ["Maria", "João", "Bruno"]

for cliente in clientes:
    print(
        email_tmpl
        % { 
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "http//canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5
        }
    )