# A fábrica de doces precisa de ajuda para embalar os doces corretamente. Cada 
# pacote deve conter um número inteiro de doces. Peça ao usuário para inserir o 
# número de doces produzidos e o número de pacotes disponíveis. Divida os doces 
# igualmente entre os pacotes fazendo a divisão inteira para garantir que cada 
# pacote contém um número inteiro de doces. Imprima o número de doces em cada pacote.

NumDoces = int(input("Qual o número total de doces?\n➥ "))
NumPacot = int(input(f"Quantos pacotes tem para embalas os {NumDoces} doces?\n➥ "))

if NumDoces%NumPacot == 0:
    print(f"Para embalar {NumDoces} doces colocaremos {NumDoces//NumPacot} doces por pacote. Bom trabalho! :)")
else:
    print(f"Para embalar {NumDoces} doces colocaremos {NumDoces//NumPacot} doces por pacote.\nE sobrará {NumDoces%NumPacot} em estoque. Bom trabalho! :)")
