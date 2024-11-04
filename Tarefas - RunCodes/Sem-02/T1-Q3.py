cores = {red:="\033[1;31m", green:="\033[1;32m", yeloow:="\033[1;33m"}

print(" Soma & Multiplicação ".center(80,"█"))
n1 = float(input(red+"\nDigite um número: "))
n2 = float(input("Digite outro número: "))

soma = print(green+f"\nA soma entre {n1:.0f}+{n2:.0f} é {(n1+n2):.0f}")
multiplicação = print(f"A multiplicação entre {n1:.0f}x{n2:.0f} é {(n1*n2):.0f}")
