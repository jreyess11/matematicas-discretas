# @author Jose Reyes
import msvcrt


def desc(n):
    primos = []
    for i in range(2, n + 1):
        if n % i == 0:
            primos.append(i)
            n = n / i
    return primos


N = int(input("Ingrese el número a descomponer: "))
print(desc(N))

msvcrt.getch()
