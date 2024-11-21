# Você sabia que os pinguins usam jaquetas devido ao frio na Antártida? 
# Vamos ajudá-los a converter temperaturas! Escreva um programa que leia 
# uma temperatura em Celsius e mostre o resultado em Fahrenheit. Lembre-se:
# Fahrenheit = (Celsius x (9 / 5)) + 32 

def main():
    print(" Conversor de Celsius para Fahrenheit ".center(60, "="))
    Celsius = float(input("\nDigite a temperatura em Celsius: "))
    Fahrenheit = (Celsius * (9 / 5)) + 32

    print(f"\n{Celsius}°C convertido para Fahrenheit é {Fahrenheit:.2f}°F")


if __name__ == "__main__":
    main()
