from random import * 

executa = True 
adjetivos = [ "maravilhoso", "acima da média", "excelente", "excepcional", "bom"] 
hobbies = [ "andar de bicicleta", "programar", "culinária", "chá", "leitura"] 

print("Gerador de Cumprimentos") 
print("---") 

nome = input("Qual é o seu nome?: ") 

print(''' 
Menu 
c = obter cumprimento 
a = adicionar hobby
d = remover hobby
p = imprimir hobby
q = sair ''')

while executa == True: 
    menuChoice = input("\n>>> ").lower() 
 
    if menuChoice == 'c':
        print(f"Aqui está o seu cumprimento {nome}" )  
        print(f"{nome} você é {choice(adjetivos)} em {choice(hobbies)}") 
        print("De nada!" )   

    elif menuChoice == "a":
        adcItem = input("Adicionar Hobbie: ")
        if adcItem not in hobbies:
            hobbies.append(adcItem)      
        else:
            print("ERROR: Hobbie já existente no banco.")

    elif menuChoice == "d":
        remov_hobbie = input("insira o hobbie a ser removido: ")
        if remov_hobbie in hobbies:
            hobbies.remove(remov_hobbie)
        else:
            print("ERROR: O hobbie não está na lista.")
    
    elif menuChoice == "p":
        print(hobbies)      
    
    elif menuChoice == 'q': 
        executa = False 
    
    else:
        print("Escolha uma opção válida")

