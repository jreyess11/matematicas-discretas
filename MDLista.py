import msvcrt

# @author Jose Reyes

def primo(n):
    for i in range(1, n+1):
        if (n % i) == 0:
            lista.append(i)

while True:
    try:
        N = int(input("Ingrese un número entero positivo: "))
        lista = []
        if N > 0:
            primo(N)
            print(f"Los divisores de {N} son: {str(lista)[1:-1]}")
            break
    except:
        print("Ingrese un número ENTERO")

msvcrt.getch()