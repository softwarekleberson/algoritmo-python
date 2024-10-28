def quicksort(array):
    if len(array) < 2:
        return array
    
    else:
        pivo = array[0]
        menor = [i for i in array[1:] if i <= pivo]
        maior = [i for i in array[1:] if i > pivo]
    
    return quicksort(menor) + [pivo] + quicksort(maior)

array = [1,0,-8,40,20,50,9,10,10,0]
print(quicksort(array))

# a cada chamada recursiva, ele pega o elemento que está na posição [0], verifica os maiores e menores e insere na lista.

#sempre quebrando o problema em varias subpartes menores
