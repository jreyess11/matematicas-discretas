# @author Jose Reyes
import msvcrt
import string
import pyfiglet


def multiply(mat1, mat2, n):
    E3 = []
    for i in range(n):
        F3 = []
        for k in range(n):
            sum = 0
            j = 0
            cont = 0
            while cont < n:
                sum += mat1[i][j] * mat2[j][k]
                j += 1
                cont += 1
            F3.append(sum)
        E3.append(F3)

    #  print("\nLas matrices multiplicadas dan:")
        #  for x in range(len(E3)):
        #     print("[", end="\t")
        #     for y in range(len(E3[x])):
        #         print(E3[x][y], end="\t")
    #     print("]")
    return E3


def exp(mat, power, n):
    aux = 1
    EP = mat
    while aux < power:
        EP = multiply(mat, EP, n)
        aux += 1

    print(f"\nLas matriz elevada a la {power} da:")
    for x in range(len(EP)):
        print("[", end="\t")
        for y in range(len(EP[x])):
            print(EP[x][y], end="\t")
        print("]")


while True:
    try:
        print(pyfiglet.figlet_format("GRAFOS"))
        V = []
        N = int(input("Ingrese el tamaño n de su matriz (nxn): "))
        E = []
        E2 = []
        for i in range(N):
            V.append(string.ascii_lowercase[i])

        print("Ingrese el contenido de la matriz 1")
        for j in range(N):
            print(f"\nFila {j + 1}:")
            F = []
            for k in range(N):
                x = int(input(f"[{V[j]},{V[k]}] = "))
                F.append(x)
            E.append(F)

        #    print("Ingrese el contenido de la matriz 2")
        #    for j in range(N):
        #        print(f"\nFila {j + 1}:")
            # F2 = []
            # for k in range(N):
            #     x = int(input(f"[{V[j]},{V[k]}] = "))
            #      F2.append(x)
        #   E2.append(F2)

        print("\nSu matriz 1 es:")
        for x in range(len(E)):
            print("[", end="\t")
            for y in range(len(E[x])):
                print(E[x][y], end="\t")
            print("]")

        #   print("\nSu matriz 2 es:")
            #  for x in range(len(E2)):
            #      print("[", end="\t")
            #      for y in range(len(E2[x])):
            #          print(E2[x][y], end="\t")
        #      print("]")

        #  print("\nVamos a multiplicar sus matrices:")
        #   multiply(E, E2, N)

        po = int(input("\nIngrese un exponente para elevar la matriz: "))
        if po == 1:
            print("Su matriz quedó igual")
        else:
            exp(E, po, N)
        break
    except:
        print("Error")

msvcrt.getch()
