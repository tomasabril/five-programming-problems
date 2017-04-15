#!/usr/bin/env python3

# ----------------
# Tomás Abril
# ----------------
import time

quantos = 430000

print("\n--modo recursivo")
# --- muito lento, só calculei até 50
func_time = time.time()
fibs = []
def fib_nmbrs(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib_nmbrs(num-1) + fib_nmbrs(num-2)
nums = [fib_nmbrs(x) for x in range(quantos)]
#print(nums)
time_t = time.time() - func_time
print("--- total time: " + str(time_t))
print("--- per number time: " + str(time_t/quantos))
# ------------


print("\n--modo aumentando lista")
# --- consome toda minha memoria com 500000 numeros
func_time = time.time()
fibs = [0, 1]
for i in range(2, quantos):
    fibs.append(fibs[i-1] + fibs[i-2])
#print(fibs)
time_t = time.time() - func_time
print("--- total time: " + str(time_t))
print("--- per number time: " + str(time_t/quantos))
# ------------

print("\n--modo preenchendo lista recursivo")
# --- parece bom, mas chega no limite de recurção do python, um pouco mais
#     lento que outras opcoes
func_time = time.time()
table = [0]*(quantos+1)
def fastfib(n):
    if n <= 1:
        return n
    else:
        if(table[n-1] == 0):
            table[n-1] = fastfib(n-1)
        if(table[n-2] == 0):
            table[n-2] = fastfib(n-2)
        table[n] = table[n-1] + table[n-2]
        return table[n]
fastfib(quantos)
#print([table[x] for x in range(quantos)])
time_t = time.time() - func_time
print("--- total time: " + str(time_t))
print("--- per number time: " + str(time_t/quantos))
# ------------


print("\n--most pythonic?")
# --- bem pouco mais rapido que o aumentando lista, tambem consome toda a
#     memoria com meio milhao de numeros
func_time = time.time()
def fibonacci():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b
fib = fibonacci()
fib_nums = [next(fib) for _ in range(quantos)]
#print(fib_nums)
time_t = time.time() - func_time
print("--- total time: " + str(time_t))
print("--- per number time: " + str(time_t/quantos))
# ------------








