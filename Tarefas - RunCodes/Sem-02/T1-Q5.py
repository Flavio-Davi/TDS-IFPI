def gol(x):
    o = ""
    if x != 0:
        for c in range(0, x):
            o += "o"
        print(f"G{o}l!")
    else:
        return print("Gol")

cores = {red:="\033[1;31m", green:="\033[1;32m", yeloow:="\033[1;33m"}
impogalcao = int(input(yeloow+"Qual o seu nível de empolgação?\n➥ "+green))
gol(impogalcao)
