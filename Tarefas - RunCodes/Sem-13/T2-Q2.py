# Escreva um programa que leia uma lista com 100 números. Ao término da leitura o 
# programa deve fazer a ordenação dos números lidos. Após a ordenação, crie uma 
# lista onde os elementos de índice PAR são multiplicados por 3 e os elementos de 
# índice ÍMPAR são multiplicados com 5. DICA: Use a função a sorted() ou o método 
# sort() para realizar a ordenação dos valores.

dados = list()
print(" MULTIPLICAÇÃO DE PARES POR 3 E ÍMPARES POR 5 ".center(60, "#"))
for c in range(100):
    dados.append(int(input(f"Número {c} de 100: ")))
dados.sort()

new_dados = list()
for i in range(len(dados)):
    if i%2 == 0:
        new_dados.append(dados[i]*3)
    else: new_dados.append(dados[i]*5)

print(f"Novos Dados: {new_dados}")
