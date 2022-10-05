lista = [3,2,4]

def iloczyn(lista):
    il = 1
    for x in lista:
        il *= x
    return il

print(iloczyn(lista))
