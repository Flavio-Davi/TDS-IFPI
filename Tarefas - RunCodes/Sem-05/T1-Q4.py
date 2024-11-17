# Escreva um programa que leia uma determinada quantidade de minutos e 
# informe essa quantidade convertidade para horas e minutos. Por exemplo, 
# 220 minutos é equivalente 3 horas e 40 minutos.

def HorasMinut(minuto):
    horas = minuto//60
    minutos = minuto%60

    return f"{horas} horas e {minutos} minutos"


def main():
    UserMinut = int(input("Digite o n° de minutos: ")).strip()
    print(HorasMinut(UserMinut))


if __name__ == "__main__":
    main()
