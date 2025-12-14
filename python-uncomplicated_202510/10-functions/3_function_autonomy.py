"""\
This is an annotation module.
"""

# definition or attribution
# signature + type hints
# documentation / docstring
# code
# return value

# - parameters
# positional - given in order


def function_name(a, b, c):
    """Esta função faz algo com a, b e c.

    Use esta função quando quiser a + b + c
    quando o parametro a tiver o value 10
    vai acontecer x.

    >>> function_name(1, 2, 3)
    6
    """
    result = a + b + c
    return result


# passagem de argumentos posicionais
value = function_name(1, 2, 3)

# passagem de argumentos nomeados
value = function_name(a=1, b=2, c=3)
value = function_name(c=1, b=2, a=3)
value = function_name(b=1, a=2, c=3)

# passagem de argumentos mista
# argumentos posicionais antes dos nomeados
value = function_name(1, 2, c=3)
value = function_name(1, c=2, b=3)

# funcao com muitos argumentos
value = function_name(
    1,
    c=2,
    b=3,
)

print(value)


###########################


def outra_funcao(a, b, c):
    """Explica o que ela faz"""
    # tupla como value de retorno
    return a * 2, b * 2, c * 2


value1, value2, value3 = outra_funcao(1, 2, 3)
print(value1)
print(value2)
print(value3)

value1, *resto = outra_funcao(1, 2, 3)
print(value1)
print(resto)


################################


# Passagem de argumentos com desempacotamento


def soma(n1, n2):
    """Faz a soma de 2 numeros."""
    return n1 + n2


# normal
print(soma(10, 20))

# argumentos em sequencia / posicional
args = (20, 30)  # tuple, list, str
# print(soma(args[0], args[1]))
print(soma(*args))


# argumentos dicionario / nomeados
args = {"n2": 90, "n1": 100}  # dict, hashmap
# print(soma(n1=args["n1"], n2=args["n2"]))
print(soma(**args))

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 100},
    {"n2": 90, "n1": 200},
    {"n2": 9, "n1": 650},
    (5, 10),
    [8, 13],
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item))
    else:
        print(soma(*item))


###############################
