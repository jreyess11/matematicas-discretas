# @author Jose Reyes
import msvcrt

print("Algoritmo extendido de Euclides.\n")


def mcd(a, b):
    a1, b1, a2, b2 = 1, 0, 0, 1
    a, b = max(a, b), min(a, b)

    while a % b != 0:
        coe = a // b

        a1 = a1 - coe * b1
        y = a1
        a1, b1 = b1, y

        a2 = a2 - coe * b2
        x = a2
        a2, b2 = b2, x

        a, b = b, a % b

    return x, y


print(mcd(13, 480))

msvcrt.getch()
