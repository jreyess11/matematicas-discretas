# @author Jose Reyes
import msvcrt
from prettytable import PrettyTable

valores = [True, False]
valor = []

print("\nEJERCICIO 50")


def P():
    P = (p and not q) or r
    return P


def Q():
    Q = not p or (not q or r)
    return Q


print("p\tq\tr\tP <-> Q")
print("-" * 25)
for p in valores:
    for q in valores:
        for r in valores:
            R = ((not P() or Q()) and (not Q() or P()))
            print(p, q, r, R, sep="\t")
            valor.append(R)

if valor.count(False) > 0:
    print("\nNo es una tautología.")
else:
    print("\nEs una tautología.")

msvcrt.getch()
