
def soma(a, b):
    return a + b

soma(1, 3)
soma(1, b=3)

def hello(nome, sobrenome="Sabugosa"):
    print(f"Hello {nome}, {sobrenome}")

hello("Raquel", "Marques")
hello("Raquel", sobrenome="Marques")
hello(sobrenome="Marques", nome="Marques")
hello("Raquel")

############

# SOLID - Single Responsibility
def funcao(*args, timeout=10, **options): # **kwargs = key word arguments
    for item in args:
        print(item)
    print(options)

    print(f"timeout {timeout}")


funcao(
    "Bruno",
    1,
    True,
    timeout=90,
    nome="Joao",
    cidade="Viana",
    data="hoje",
    banana=1,
    panela=3,
    teclado=True,
)
