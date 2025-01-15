# Escreva um programa que, para um número indeterminado de pessoas:
#   leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag) e não deve ser considerada;
#   calcule e escreva o número de pessoas;
#   calcule e escreva a idade média do grupo;
#   calcule e escreva a menor idade e a maior idade.

def main():
    user = int(input())
    numPessoas = 0
    all = list()

    while user != 0:
        all.append(user)
        numPessoas += 1
        user = int(input())

    menorIdade = min(all)
    maiorIdade = max(all)
    mediaIdade = sum(all)/len(all)

    print(f"{numPessoas}\n{mediaIdade:.2f}\n{menorIdade}\n{maiorIdade}")


if __name__ == "__main__":
    main()
