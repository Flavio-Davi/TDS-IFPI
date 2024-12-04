# Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: 
# dia, mês e ano) e escreva qual delas é a mais recente.

def recent_date(date1, date2):
    recent = False if date1[2] > date2[2] else date2[2] > date1[2] # SE False date2 maior, SE false date2 maior.

    if date1[2] == date2[2] and date1[1] != date2[1]:
        recent = False if date1[1] > date2[1] else date2[1] > date1[1] # SE False date2 maior, SE false date2 maior.
    elif date1[1] == date2[1] and date1[2] == date2[2]:
        recent = False if date1[0] > date2[0] else date2[0] > date1[0] # SE False date2 maior, SE false date2 maior.
    
    return date1 if recent == False else date2


data1 = list()
data2 = list()
descricao = ["Dia", "Mês", "Ano"]

print(" PROGRAMA DE DATA MAIS RECENTE ".center(40, "@"))
for c in range(3):
    data1.append(int(input(f"{descricao[c]}: ")))
for c in range(3):
    data2.append(int(input(f"{descricao[c]}: ")))
    
menor_data = "/".join(str(data) for data in recent_date(data1, data2))
print(f"A menor data digitada é {menor_data}")

