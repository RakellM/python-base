"""Function examples"""

"""
f(x) = 5 * (x / 2)
"""

# Solid - Single Responsibility

def f(x): 
    result = 5 * (x / 2)
    return result

print(f(10))
print(f(10) == 25)

def double(x):
    return x * 2

value = double(f(10))
print(value)
print(value == 50)

def print_in_upper(text):
    """Procedure with no return"""
    print(text.upper())

print_in_upper("raquel")



def heron(a, b, c):
    """Calculate the area of a triangle."""
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area ** 0.5 # math.sqrt(area)

def heron2(params):
    # a, b, c = params
    # return heron(a, b, c)
    return heron(*params)

area_triangle = heron(3, 4, 5)
print(area_triangle)

triagles = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
]

for t in triagles:
    # area = heron(t[0], t[1], t[2])
    # area = heron(*t)
    area = heron2(t)
    print(f"The area of the triangle is: {area}")


print(list(map(heron2, triagles)))



###



