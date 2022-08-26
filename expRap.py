# @author Jose Reyes
import msvcrt
import pyfiglet


def convBin(n):
    r = []
    while n // 2 != 0:
        r.append(n % 2)
        coef = n // 2
        n = coef
    if n // 2 == 0:
        r.append(n % 2)
        return r


def expRap(exp):
    p = 0
    r = []
    print(convBin(exp))
    for j in convBin(exp):
        if j == 1:
            r.append(pow(2, p))
        p += 1
    return r


while True:
    try:
        print(pyfiglet.figlet_format("BDAY BOYYYY"))
        X = int(input("Ingrese un número x: "))
        N = int(input("Ingrese el exponente n: "))
        print(f"{X}^{N} es igual a:")
        for i in expRap(N):
            print(f"{X}^{i}", end="  ")
        break
    except:
        print("Ingrese números válidos.")

msvcrt.getch()
