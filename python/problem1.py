#!/usr/bin/env python3

# ----------------
# Tomás Abril
# ----------------

import random

list = [random.randint(0, 100) for x in range(15)]
print(list)

sum = 0
for i in list:
    sum += i
print(sum)

sum = 0
list_cpy = list[:]
while(list_cpy):
    sum += list_cpy.pop()
print(sum)


def calcula_soma(index, lst):
    if index == len(lst):
        return 0
    else:
        return lst[index] + calcula_soma(index + 1, lst)


print(calcula_soma(0, list[:]))
