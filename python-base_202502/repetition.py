#!/usr/bin/env python3

# FOR

#numbers = [1,2,3,4,5,6]
numbers = range(1, 11) #start, next, stop

# Iterable - continue
for number in numbers:
    even = number % 2 == 0
    if even:
        print(number)
    else:
        continue

    print(f"more codes with {number}")

print("---")

# Iterable - break
for number in numbers:
    odd = number % 2 != 0
    if odd:
        print(number)
    else:
        break

    print(f"more codes with {number}")

print("---")

# For loops: line-by-line
original_list = [1, 2, 3]
new_list = []
for n in original_list:
    new_list.append(n * 2)

print(new_list)

# For loops: functional
# List Comprehension
new_list2 = [n * 2 for n in original_list]
print(new_list2)

# List Comprehension
raw_list = [line for line in open("post.txt") if ":" in line]
print(raw_list)

# Dict Comprehension
raw_dict = {
    line.split(":")[0]: line.split(":")[1].strip() 
    for line in open("post.txt") 
    if ":" in line
}
print(raw_dict)

# It is the same as
raw_dict2 = {}
for line in open("post.txt"):
    if ":" in line:
        key, value = line.split(":")
        raw_dict2[key] = value.strip()

print(raw_dict2)

###########################################################
# WHILE
n = 0
#while True: # main loop / infinity loop
while n < 101: # stop condition
    if n >= 20 and n <= 30:
        n += 1 # if not added you enter on a dead lock
        continue #skip the numbers
    if n == 40:
        break
    print(n)
    n += 1
