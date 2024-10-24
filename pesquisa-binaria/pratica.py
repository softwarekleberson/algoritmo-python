def busca_binaria(arr, item):
    menor = 0
    maior = len(arr) - 1

    while menor < maior:
        meio = (menor + maior) // 2
        chute = arr[meio]

        if chute == item:
            return meio
        
        if chute > item:
            maior = meio - 1
        
        else:
            menor = meio + 1
    
    return None

elemento = [1,2,3,4,5,6,7,8,9,10]
print(busca_binaria(elemento, 8))