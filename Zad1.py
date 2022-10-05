#a
lista1 = []
for x in range(1,11):
    lista1.append(x)
print(lista1)

#b
lista2 = []
for x in range(0,22,2):
    lista2.append(x)
print(lista2)

lista3 = []
for x in range(1,11,1):
    lista3.append(pow(x,2))
print(lista3)

lista4 = []
for x in range(0,10,1):
    lista4.append(0)
print(lista4)

lista5 = []
for x in range(0,5,1):
    for x in range(0,2):
        lista5.append(x)
print(lista5)

lista6 = []
for x in range(0,2,1):
    for x in range(0,5):
        lista6.append(x)
print(lista6)
