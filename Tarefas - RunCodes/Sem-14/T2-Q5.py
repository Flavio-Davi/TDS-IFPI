# Faça um programa que leia duas listas de 10 elementos. Crie uma lista que seja a 
# união entre as 2 listas anteriores, ou seja, que contêm os números das duas listas. 
# Não deve conter números repetidos.

def list_unica(list_1, list_2):
    end_list = list()

    for c in list_1:
        if c not in end_list:
            end_list.append(c)
    for c in list_2:
        if c not in end_list:
            end_list.append(c)

    return end_list


def main():
    list_1 = list()
    list_2 = list()
    
    for _ in range(10):
        list_1.append(int(input()))
    for _ in range(10):
        list_2.append(int(input()))

    print(list_unica(list_1, list_2))
    

if __name__ == '__main__':
    main()
