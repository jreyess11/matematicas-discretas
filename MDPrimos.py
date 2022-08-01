import msvcrt
import math

# @author Jose Reyes

def primo(n):
    for i in range(2, int(n/2)):
        if (n % i) == 0:
            return False
    return True

while True:
    try:
        N = int(input("Ingrese un número entero positivo: "))
        if N > 1:
            if primo(N):
                print(f"{N} es un número primo")
                break
            else:
                print(f"{N} es un número compuesto")
                break
    except:
        print("Ingrese un número ENTERO.")
