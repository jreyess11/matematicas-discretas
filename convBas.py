# @author Jose Reyes
import msvcrt

print("Convertir a cualquier base.\n")


def convBas(n, b):
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L',
           22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X',
           34: 'Y', 35: 'Z'}
    r = []
    while n // b != 0:
        r.append(n % b)
        coef = n // b
        n = coef
    r.append(n % b)
    if b >= 16:
        for i in range(len(r)):
            if r[i] in dic:
                r[i] = dic[r[i]]
    r.reverse()
    return r


while True:
    try:
        N = int(input("Ingrese un número n: "))
        B = int(input("Ingrese la base mayor a 1: "))
        print(f"El numero {N} en base {B} es ")
        print(*convBas(N, B), sep="")
        break
    except:
        print("Ingrese números válidos.")

msvcrt.getch()
