# @author Jose Reyes
import math
import msvcrt
import pyfiglet

print("Convertir a cualquier base.\n")


def cantor(x):
    fact = 2
    og = x
    div = []
    div.append("1!")
    res = []
    while math.factorial(fact) <= og:
        div.append(f"{fact}!")
        i = x % fact
        x = x // fact
        res.append(i)
        fact += 1
    i = x % fact
    res.append(i)
    div.reverse()
    res.reverse()
    return div, res


while True:
    try:
        print(pyfiglet.figlet_format("CANTOR"))
        X = int(input("Ingrese el numero x: "))
        if (X <= 0):
            raise ValueError()
        res = f"{X} = "
        aux1, aux2 = cantor(X)
        for i in range(len(aux1)):
            res += f"{aux1[i]}({aux2[i]}) + "
        print(res[0:-3])
        break
    except:
        print("\nIngrese números válidos.")

msvcrt.getch()
