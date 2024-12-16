# Escreva um programa que leia um número e exiba o dia correspobndente da semana. 
# (1-domingo,2-segunda-feira,3-terça-feira), se digitar outro valor deve aparecer "valor inválido".

def dia_semana(number):
    semana = {"1":"domingo","2":"segunda-feira","3":"terça-feira","4":"quarta-feira","5":"quinta-feira","6":"sexta-feira","7":"sábado"}
    
    for key, value in semana.items():
        if key == number:
            return value
    return "valor inválido"


def main():
    print(" DIA DA SEMANA(1-7) ".center(44, "@"))
    user = input("\nDigite um número que represente o dia da semana: ").strip()
    
    print(f"O número digitado representa, {dia_semana(user)}")


if __name__ == '__main__':
    main()
