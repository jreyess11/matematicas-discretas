# @author Jose Reyes
import msvcrt


def desc(n):
    primos = []
    for x in range(2, n + 1):
        while n % x == 0:
            primos.append(x)
            n = n / x
    return primos


N = int(input("Ingrese el número a descomponer: "))
print(*desc(N), sep=" * ")

msvcrt.getch()
