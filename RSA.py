# @author Jose Reyes
import msvcrt
import pyfiglet

p = 59
q = 37
n = p * q
O = (p - 1) * (q - 1)
e = 17
d = 737

while True:
    try:
        print(pyfiglet.figlet_format("RSA"))
        print("\033[1;33m" + "Ingrese su mensaje: " + "\033[0;m")
        str = input("")
        str2 = ""
        m = []
        x = []
        des = []
        for i in str.lower():
            if i == " ":
                m.append("-")
            else:
                m.append(ord(i))
        for j in m:
            if j == "-":
                x.append("-")
                continue
            x.append((pow(j, e) % n))
        print("\033[1;31m", "Su mensaje encriptado es: ", *x, "\033[0;m")
        #Descifrar
        for k in x:
            if k == "-":
                des.append("-")
                continue
            des.append((pow(k, d) % n))
        print("\033[1;36m", "Su mensaje descifrado es: ", *des, "\033[0;m")

        for l in des:
            if l == "-":
                str2 += " "
                continue
            str2 += chr(l)

        print("Su mensaje original es:", str2)
        break
    except:
        print("Ocurrió un error.")

msvcrt.getch()
