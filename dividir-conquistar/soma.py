def soma_recursiva(lista):
    if not lista:
        return 0
    
    return lista[0] + soma_recursiva(lista[1:])

lista = [1,2,3,4,5,6]
print(soma_recursiva(lista))