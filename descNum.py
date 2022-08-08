# @author Jose Reyes
import msvcrt
import math



def primo(n):
    primos = []
    r = int(math.sqrt(n))
    for i in range(2, r+1):
        if (n % i) == 0:
            primos.append(i)
    return primos


def desc(n):
    lista = []
    for j in primo(n):
        while n % j == 0:
            lista.append(j)
            n = n/j
    return lista


while True:
    try:
        N = int(input("Ingrese un número entero positivo para descomponer: "))
        if N > 0:
            print(primo(N))
            print(*desc(N), sep=" * ")
            break
    except:
        print("Ingrese un numero entero POSITIVO")

msvcrt.getch()
