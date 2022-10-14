# @author Jose Reyes
import msvcrt
import string

import pyfiglet


def multiply(mat1, mat2, n):
    sum = 0
    for i in range(n):
        sum += mat1[n] * mat2[:n]


while True:
    try:
        print(pyfiglet.figlet_format("GRAFOS"))
        V = []
        N = int(input("Ingrese el tamaño n de su matriz (nxn): "))
        E = []
        F = []
        for i in range(N):
            V.append(string.ascii_lowercase[i])

        print("Ingrese el contenido de la matriz")
        for j in range(N):
            print(f"\nFila {j + 1}:")
            F = []
            for k in range(N):
                x = int(input(f"[{V[j]},{V[k]}] = "))
                F.append(x)
            E.append(F)

        print("\nSu matriz es:")
        for x in range(len(E)):
            print("[", end="\t")
            for y in range(len(E[x])):
                print(E[x][y], end="\t")
            print("]")
        break
    except:
        print("Error")

msvcrt.getch()
