a = [1, 2, 3]
b = [4, 5, 6]
c = []

for dado in zip(a, b):
    for i in dado:
        c.append(i)
print(c)  

 