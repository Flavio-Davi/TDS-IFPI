# Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a) "Telefonou para a vítima ?"
# b) "Esteve no local do crime ?"
# c) "Mora perto da vítima ?"
# d) "Devia para a vítima ?"
# e) "Já trabalhou com a vítima ?"
# Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação
# da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 
# "Suspeito", entre 3 ou 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado 
# como "Inocente".

def classificacao(pg1, pg2, pg3, pg4, pg5):
    total = pg1 + pg2 + pg3 + pg4 + pg5
    if total.count("S") == 2:
        return "Suspeito"
    elif total.count("S") == 5:
        return "Assassino"
    elif 5 > total.count("S") > 2:
        return "Cúmplice"
    else:
        return "Inocente"


def main():
    print("  CLASSIFICAÇÃO DE SUSPEITO ".center(44, "@"))
    pg1 = input("Telefonou para a vítima?[S/N] ").strip()[0]
    pg2 = input("Esteve no local do crime?[S/N] ").strip()[0]
    pg3 = input("Mora perto da vítima?[S/N] ").strip()[0]
    pg4 = input("Devia para a vítima?[S/N] ").strip()[0]
    pg5 = input("Já trabalhou com a vítima?[S/N] ").strip()[0]
   
    print(f"\nSua calassificação é {classificacao(pg1, pg2, pg3, pg4, pg5)}!")


if __name__ == '__main__':
    main()
