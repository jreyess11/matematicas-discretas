# @author Jose Reyes
import msvcrt
import math


def desc(n):
    primos = []
    for x in range(2, r):
        while n % x == 0:
            primos.append(x)
            n = n / x
    return primos

while True:
    try:
        N = int(input("Ingrese un número entero positivo para descomponer: "))
        if N>0:
            print(*desc(N), sep=" * ")
            break
    except:
        print("Ingrese un numero entero POSITIVO")

msvcrt.getch()