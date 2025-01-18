# Escreva um programa Python que apresente o menu de opções abaixo:
# OPÇÕES: 1 - SAUDAÇÃO 2 - BRONCA 3 - FELICITAÇÃO 0 - FIM
# O programa deve ler a opção do usuário e exibir, para cada opção, a respectiva mensagem:
# 1 - Olá. Como vai? 2 - Vamos estudar mais. 3 - Meus Parabéns! 0 - Fim de serviço.
# Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção inválida.”. Enquanto a opção for diferente de 0 (zero)# deve-se continuar apresentando as opções. Obs: use como estrutura de repetição com teste no final e como estrutura condicional # # # múltipla escolha.


menu = {"1 - SAUDAÇÃO": "1 - Olá. Como vai?", "2 - BRONCA": "2 - Vamos estudar mais.", "3 - FELICITAÇÃO": "3 - Meus Parabéns!", "0 - FIM": "0 - Fim de serviço."}
user = None

while user != "0":
    user = input(f"OPÇÕES:\n{'\n'.join(map(str, menu.keys()))}\n").strip()
    
    if user == "0":
        print(menu["0 - FIM"])
    elif user == "1":
        print(menu["1 - SAUDAÇÃO"])
    elif user == "2":
        print(menu["2 - BRONCA"])
    elif user == "3":
        print(menu["3 - FELICITAÇÃO"])
    else:
        print("Opção inválida.")
    
