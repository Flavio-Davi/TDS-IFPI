# Escreva um programa que leia um número n. Considere uma lista com n posições,
# e então: a) preencha com 0 (zero) e  imprima a lista; b) preencha com os
# números de 1 a n e imprima a lista; c) preencha com valores lidos pelo
# teclado e imprima a lista; d) preencha  na ordem inversa com valores lidos 
# pelo teclado e imprima a lista; dica: use insert para sempre incluir
# os elementos no início da lista;

class analise():
    def __init__(self):
        self.home()
        
        
    def apresentar(self, lista1, lista2):
        list_zero = list()
        list_cresc = list()
        list_real = lista1.copy()
        list_inve = lista2[::-1]
        
        for c in range(1, len(lista1)+1):
            list_zero.append(0)
            list_cresc.append(c)
                        
        return list_zero, list_cresc, list_real, list_inve
        
        
    def home(self):
        print(" ANÁLISE DE LISTA ".center(50, "#"))
        user = int(input("\nDigite o número de itens de suas lista: "))
        user_list1 = list()
        user_list2 = list()

        for c in range(user):
            user_list1.append(int(input(f"Lista 1 - item {c+1}: ")))
        for c in range(user):
            user_list2.append(int(input(f"Lista 2 - item {c+1}: ")))

        print("\nAnálise:")
        print("\n".join(map(str, self.apresentar(user_list1, user_list2))))


if __name__ == '__main__':
    analise()
