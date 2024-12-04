# Escreva um programa que leia, separadamente, dia, mês e ano da data atual. 
# Leia, da mesma forma, a data de nascimento de uma pessoa, calcule e escreva a idade exata em anos

def idade(hoje, nascimento):
    anos = hoje[2] - nascimento[2]    

    if hoje[1] < nascimento[1]:
        anos -= 1
    elif  hoje[0] < nascimento[0] and hoje[1] <= nascimento[1]:
        anos -=1
    return anos


data_atua = list()
data_nasc = list()
descricao = ["Data", "Mês", "Ano"]

print(" CALCULADORA DE IDADE ".center(44, "#"))

print("\nDigite a data a atual a baixo")
for c in range(3):
    data_atua.append(int(input(f"{descricao[c]}: ")))
print("\nAgora digite sua data de nascimento a baixo")
for c in range(3):
    data_nasc.append(int(input(f"{descricao[c]}: ")))

print(f"\nSua idade é {idade(data_atua, data_nasc)} anos.")
