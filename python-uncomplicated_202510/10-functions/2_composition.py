"""Print only names that starts with letter B"""

names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barbara",
    "Brian",
]


# Functional Style
print("Functional style")
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")

print()

# Procedure Style
print("EProcedure style")


def starts_with_b(text):
    """Return bool if text starts with b"""
    return text[0].lower() == "b"


filter_ = filter(starts_with_b, names)
filter_ = list(filter_)
for name in filter_:
    print(name)
