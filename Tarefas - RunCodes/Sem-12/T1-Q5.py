# O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha Maurítius, na costa leste da África. 
# A partir do ano 1600, durante cada ano, 6% dos animais dos animais vivos no começo do ano morreram e o número de 
# animais nascidos ao longo do ano que sobreviveram foi de 1% da população inicial.
# Escreva um programa que leia a população de aves no início do ano 1600 e 
# imprime, anualmente, a partir do fim de 
# 1600, o número de nascimentos, mortes e o total da população por ano (apenas a parte inteira do números, separados
# por vírgula). O programa encerra sua execução quanto a população total cai para menos de 10% da população original.
# ANO, N° NASC, N° N° DE MORTOS,  
class Dodo():
    def __init__(self):
        self.user()


    def calcularAnos(self, popInicial):
        allData = {"ano": list(), "nascidos": list(), "mortes": list(), "total": list()}
        kill = 0.06 # começo do ano morreram
        born = 0.01 # da população inicial
        parar = round(popInicial*0.1)
        ano = 1599
        total = popInicial

        while total > parar:
            ano += 1
            mortes = total*kill
            nascidos = total*born
            total =  total-mortes+nascidos

            allData["ano"].append(ano)
            allData["mortes"].append(mortes)
            allData["nascidos"].append(nascidos)
            allData["total"].append(total)


        return allData


    def user(self):
        popAves = float(input("Descreva o n° da população de dodô no início de 1600: ")) # Leia a população de aves no início do ano 1600 
        data = self.calcularAnos(popAves)

        print(f"{'ANO':<10}{'NASCIDOS':<11}{'MORTOS':>7}{'TOTAL':>11}")
        for ano, morte, nascido, total in zip(data["ano"], data["nascidos"], data["mortes"], data["total"]):
            print(f"{round(ano):<10} {round(morte):<10} {round(nascido):<10} {round(total):>10}")

Dodo()
