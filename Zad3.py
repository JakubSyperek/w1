lista = [1,2,-3,4,-5]

def ile_ujemnych(lista):
    count = 0
    for x in lista:
        if(x>0):
            count += 1
    return count

print(ile_ujemnych(lista))