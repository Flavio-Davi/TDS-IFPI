# Escreva um programa que leia o tempo de duração de um evento em 
# uma fábrica expresso em segundos. Calcule e exiba esse tempo em horas, minutos e segundos (HH:MM:SS).

def conversor(TimeSeg):
    horas = TimeSeg//3600
    minutos = TimeSeg//60 - 60*horas  
    segundos = TimeSeg%60

    return f"{horas}:{minutos}:{segundos}"


def main():
    print(" Conversor de segundos para HH:MM:SS ".center(55, "="))
    
    user = int(input("\nDigite o n° de segudos: "))
    print(f"\n{user}segundos convertidos é {conversor(user)}")

if __name__ == "__main__":
    main()
