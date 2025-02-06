# Escreva um programa que ler dois conjuntos de números reais, armazenando-os em listas e 
# calcule o produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois 
# conjuntos e o produto escalar, sendo que o produto escalar e dado por: 
# (x1*y1 )+(x2*y2 )+(x3*y3 )+⋯+(xn*yn). Por exemplo, para as duas listas X e Y a seguir:
#       0       1       2       3       4
#  X =     2       5       7       3       9
#  Y =     3       8       1       0       4
# O produto escalar será: (2 x 3) + (5 x 8) + (7 x 1) + (3 x 0) + (9 x 4) = 89

def produto(conjunto1, conjunto2):
    conjuntos = ""
    total = 0
    
    for c in range(5):
        if c == 0:
            conjuntos += f"({conjunto1[c]} x {conjunto2[c]}) +"
        if c > 0 and c <4:
            conjuntos += f" ({conjunto1[c]} x {conjunto2[c]}) +"
        if c == 4:
            conjuntos += f" ({conjunto1[c]} x {conjunto2[c]}) "
        total += (conjunto1[c] * conjunto2[c])

    return conjuntos, total


def main():
    conjunto_x = list()
    conjunto_y = list()

    for _ in range(5):
        conjunto_x.append(int(input()))
    for _ in range(5):
        conjunto_y.append(int(input()))

    print(conjunto_x)
    print(conjunto_y)
    print("= ".join(map(str, produto(conjunto_x, conjunto_y))))


if __name__ == '__main__':
    main()
