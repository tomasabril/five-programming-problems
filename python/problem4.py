#!/usr/bin/env python3

# ----------------
# Tomás Abril
# ----------------

import random


lista = [random.randint(0, 100) for x in range(10)]
print(lista)
tam = max([len(str(x)) for x in lista])


def comp(x):
    for i in range(len(x), tam):
        x += '9'
    return x


ls = sorted(map(str, lista), key=comp, reverse=True)
print(ls)
