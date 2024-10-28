cores = {red:="\033[1;31m", green:="\033[1;32m", yeloow:="\033[1;33m", cyano:="\033[1;36m"}

Pnome = input(cyano+"Olá, qual seu primeiro nome? \n➥ ").strip()
Snome = input(f"E seu sobre nome {Pnome}, qual é? \n➥ ").strip()

print(yeloow+f"\nEste é seu nome e sobre nome\n➥ {Pnome} {Snome}")