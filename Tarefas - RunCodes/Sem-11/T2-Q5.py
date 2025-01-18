# Faça um programa que leia a nota de um aluno, entre zero e dez. Mostre a 
# mensagem “Nota inválida.” caso o valor seja inválido e continue pedindo até 
# que o usuário informe um valor válido. Após informar uma nota válida, o 
# aluno deve ver seu conceito, segundo a tabela:

def avaliar(nota):
    if 8.5 <= nota <= 10: 
        return "A"
    elif 7 <= nota < 8.5:  
        return "B"
    elif 5 <= nota < 7:  
        return "C"
    elif 4 <= nota < 6:  
        return "D"
    elif 0 <= nota < 4:  
        return "E"


def main():
    print(" AVALIADOR DE NOTAS ".center(50, "@"))
    while True:
        try:
            user = float(input("\nDigite sua nota: "))
        except ValueError:
            print(">>> Valor inserido inávlido, digite apenas números.")
            continue
        if user>10 or user<0: 
            print("Nota inválida.")
        else: 
            break
    print(f"Avaliação: {avaliar(user)}")
        

if __name__ == "__main__":
    main()
