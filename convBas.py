# @author Jose Reyes
import msvcrt


print("Convertir a cualquier base.\n")


def convBas(n, b):
    r = []
    while n//b != 0:
        r.append(n % b)
        coef = n // b
        n = coef
    if n//b == 0:
        r.append(n % b)
        r.reverse()
        return r


while True:
    try:
        N = int(input("Ingrese un número n: "))
        B = int(input("Ingrese la base mayor a 1: "))
        print(f"El numero {N} en base {B} es {convBas(N, B)}")
        break
    except:
        print("Ingrese números válidos.")

msvcrt.getch()
