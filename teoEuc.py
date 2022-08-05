# @author Jose Reyes
import msvcrt


def mcd(a, b):
    min = []
    c = 0
    if a%b==0:
        min.append(a)
        return min
    while a % b != 0:
        min.append(a % b)
        c = a
        a = b
        b = c % b
    return min


while True:
    try:
        A = int(input("Ingrese un número a: "))
        B = int(input("Ingrese un número b: "))
        temp = 0
        if A >= B:
            print(f"El máximo común divisor es {min(mcd(A, B))}")
            break
        else:
            print(f"El máximo común divisor es {min(mcd(B, A))}")
            break
    except:
        print("Ingrese números válidos.")

msvcrt.getch()
