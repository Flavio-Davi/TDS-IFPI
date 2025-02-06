# Escreva um programa para ajudar um novo dono a dar nome ao seu animal de estimação. 
# 1. Permitir que o usuario adicione e remova itens da lista;
# 2. Dar nomes diferentes para animais machos e fêmeas, ou para tipos diferentes de animais;
# 3. Perguntar quantos nomes ele precisa, caso eles tenham mais de um animal para dar nome.

class name_pet:
    def __init__(self):
        self.main()


    def dados(self, new_dado): 
        femea_nomes = ["Mel", "Jade", "Bela", "Cristal", "Frida", "Pipoca", "Aneko", "Akina", "Yuki"] 
        macho_nomes = ["Billy", "Pudim", "'Duque", "Ozzy", "Johnny", "Ted", "Rex", "Toby"] 
        all_nomes =  macho_nomes + femea_nomes
        
        return all_nomes


    def home(self):
        print(" ESCOLHENDO O NOME DE SEU PET ".center(60, "#"))
        user = input('''\n[ 1 ] - Adicionar nomes
[ 2 ] - Remover nomes
[ 3 ] - Selecionar gênero do pet
[ 4 ] - Sair\n>>> ''')

        return user
    

    def adcionar(self):
        new = input("Digite o nome que deseja adicionar: ")
        all = self.dados()
        all.append(new)

        return print(">>> Nome adicionado com sucesso!")


    def main(self):
        while True:
            user = self.home()
            if user == "1":
                self.adcionar()
            elif user == "4":
                print(">>> Até mais!")
                break
            else:
                continue


name_pet()
