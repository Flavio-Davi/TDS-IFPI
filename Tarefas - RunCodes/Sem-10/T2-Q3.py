# Modifique a canção dos programadores novamente para aumentar os bugs de 7 em 7, iniciando em 99 
# e parando em 250 ou antes 99 bugs no software, pegue um deles e conserte... Tecle “Ctrl+F5” 106 
# bugs no software, pegue um deles e conserte... Tecle “Ctrl+F5” 113 bugs no software, pegue um 
# deles e conserte... Tecle “Ctrl+F5” ... Vamos fazer mais um café!

def main():
    musica = 'bugs no software, pegue sete deles e conserte...\nTecle "Ctrl+F5"'
    for c in range(99, 251, 7):
        print(f"{c} {musica}")
    print("Vamos fazer mais um café!")


if __name__ == "__main__":
    main()
    