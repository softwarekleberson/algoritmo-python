def conta_elementos(lista):
    if not lista:
        return 0
    
    return 1 + conta_elementos(lista[1:])

lista = [1,2,3,4,5,6,7,8,9,10]
print(conta_elementos(lista))