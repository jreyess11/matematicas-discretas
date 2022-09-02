# @author Jose Reyes
import msvcrt
import pyfiglet

print("Convertir a cualquier base.\n")


def alea(cant, m):
    x0 = 2
    a = 5
    c = m - 1
    l = []
    for i in range(cant):
        x = (a * x0 + c) % m
        l.append(x)
        x0 = x
    return l


while True:
    try:
        print(pyfiglet.figlet_format("ALEATORIOS"))
        C = int(input("Ingrese la cantidad de numeros: "))
        M = int(input("Ingrese el rango: "))
        print(alea(C, M))
        break
    except:
        print("Ingrese números válidos.")

msvcrt.getch()
