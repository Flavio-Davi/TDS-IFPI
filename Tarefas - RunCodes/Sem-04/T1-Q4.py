# Você gostaria de saber quantos segundos se passaram desde a meia-noite? 
# Escreva um programa que leia valores inteiros para hora, minuto e segundo. 
# Em seguida, o programa deve calcular e imprimir quantos segundos se passaram 
# no total desde a ultima meia-noite até a hora lida.

print(" CONTADOR DE SEGUNDOS, PÓS MEIA-NOITE ".center(45, "="))

hora = int(input("Horas: "))
minuto = int(input("Minutos: "))
segundo = int(input("Segundos: "))

ApMeiaNoite = (hora*60)*60 + (minuto*60) + segundo

print(f"\nO número de segundos desde a 0h até o horário descrito é de {ApMeiaNoite}seg")
