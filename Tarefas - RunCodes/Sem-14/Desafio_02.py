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
q = sair ''')

while executa == True: 
    menuChoice = input("\n>_").lower() 
 
    if menuChoice == 'c':
        print(f"Aqui está o seu cumprimento {nome}" )  
        print(f"{nome} você é {choice(adjetivos)} em {choice(hobbies)}") 
        print("De nada!" )         
    elif menuChoice == 'q': 
        executa = False 
    else:
        print("Escolha uma opção válida")
