#!/usr/bin/env python3

# ----------------
# Tomás Abril
# ----------------

import random
import string

list1 = [random.randint(0, 9) for x in range(8)]
print(list1)

list2 = [random.choice(string.ascii_lowercase) for x in range(8)]
print(list2)

final = []
for i in range(len(list1)):
    final.append(list1[i])
    final.append(list2[i])
print(final)
