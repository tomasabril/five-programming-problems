#!/usr/bin/env python3

# ----------------
# Tomás Abril
# ----------------

import itertools

numbers = range(1, 10)
results = []

# todas as possibilidades para colocar entre os numeros
for perm in itertools.product(['+', '-', ''], repeat=(len(numbers) - 1)):
    # add something for digit 9
    tuples = zip(numbers, perm + ('', ))
    # create expression as string
    expression = ''.join([str(e1) + e2 for (e1, e2) in tuples])
    if eval(expression) == 100:
        results.append(expression + " = 100")

print('[%s]' % '\n'.join(map(str, results)))
