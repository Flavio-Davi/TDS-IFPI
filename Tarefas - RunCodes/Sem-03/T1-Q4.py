# O tempo é algo legal, especialmente quando você vai calcular quantos minutos há 
# em um número específico de segundos. Peça ao usuário para inserir um número de 
# segundos. Em seguida, use a divisão inteira para mostrar esse tempo em minutos 
# (lembre-se, 1 minuto = 60 segundos) e use o resto da divisão inteira para saber 
# quantos segundos sobram. Imprima os resultados.

print(" Conversor de segundos ".center(40, "="))
seg = int(input("\nDigite o n° de segundos\n➥ "))

print(f"\n{seg} convertido para minutos é igual a {seg//60}min{seg%60}seg")
