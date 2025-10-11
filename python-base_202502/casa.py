#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""
__version__ = "0.1.1"
__author__ = "Raquel Marques"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês" , aula_ingles), 
    ("Música", aula_musica),
    ("Dança", aula_danca),
]

# Listar alunos en cada atividade por sala

for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}")
    print("-" * 30)
    atividade_sala1 = []
    atividade_sala2 = []

    # sala1 que tem interseção com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)
    
    print()
    print("#" * 30)