def busca_binaria(lista, item):
    baixo = 0                                               # inicio da lista
    alto = len(lista) - 1                                   # total de elementos na lista

    while baixo <= alto:                                    # continue até baixo for maior
        meio = (baixo + alto) // 2                          # preciso saber o meio da lista
        chute = lista[meio]                                 # meu chute será exatamente no meio

        if chute == item:                                   # se acertei, devolva o elemento 
            return meio
        
        if chute > item:                                    # chute maior, então, preciso ir no meio - 1, esse é o novo alto
            alto = meio - 1
        else:
            baixo = meio + 1

    return None                                             # não achou o elemento


minha_lista = [1,3,7,9,12]                                  
print(busca_binaria(minha_lista, 20))