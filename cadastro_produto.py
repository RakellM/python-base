#!/usr/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.1"
__author__ = "Raquel Marques"

produto = {
    "nome": "Caneta",
    "cor1": "azul",
    "cor2": "branco",
    "preco": 3.23 ,
    "dimensao_altura": 12.1 ,
    "dimensao_largura": 0.8 ,
    "em_estoque": True ,
    "codigo": 45678 ,
    "codebar": None
}

compra = ("João", produto["nome"], 3)
total_compra = compra[2] * produto["preco"]

print(
    f"O cliente {compra[0]}"
    f" comprou {compra[1]}"
    f" e pagou o total de {total_compra}"
)