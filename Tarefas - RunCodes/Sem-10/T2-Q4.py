# Modifique mais um vez a canção dos programadores, dessa vez, gerando a canção dos bons programadores, 
# que resolvem 11 erros de cada vez e ao chegar a zero declaram que o software está estabilizado. 
# Atenção para o exemplo a seguir, especialmente, os versos finais. 99 bugs no software, pegue um deles e conserte... 
# Tecle “Ctrl+F5” 88 bugs no software, pegue um deles e conserte... Tecle “Ctrl+F5” 77 bugs no software, 
# pegue um deles e conserte... Tecle “Ctrl+F5” ... 11 bugs no software, pegue um deles e conserte... 
# Tecle “Ctrl+F5” Sem erros no software! Está estabilizado!

def main():
    musica = 'bugs no software, pegue onze deles e conserte...\nTecle "Ctrl+F5"'
    for c in range(99, 10, -11):
        print(f"{c} {musica}")
    print("Sem erros no software! Está estabilizado!")


if __name__ == "__main__":
    main()
    