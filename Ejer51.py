#@author Jose Reyes
import msvcrt

valores = [True, False]
valor = []

print("\nEJERCICIO 50")

def P():
    P=(not s or (p and not r))and(not p or (r or q)and s)
    return P
def Q():
    Q=p or t
    return Q

print("p\tq\tr\ts\tt\tP <-> Q")
print("-"*25)
for p in valores:
    for q in valores:
        for r in valores:
            for s in valores:
                for t in valores:
                    R=((not P() or Q()) and (not Q() or P()))
                    print(p,q,r,s,t,R, sep="\t")
                    valor.append(R)

if valor.count(False)>0:
    print("\nNo es una tautología.")
else:
    print("\nEs una tautología.")

msvcrt.getch()