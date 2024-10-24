def selection_sort(arr):
    # Percorre toda a lista
    for i in range(len(arr)):
        # Assume que o menor elemento está na posição i
        min_idx = i
        
        # Procura o menor elemento na parte não ordenada
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Troca o menor elemento encontrado com o elemento atual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Exemplo de uso
lista = [64, 25, 12, 22, 11]
print("Lista original:", lista)
lista_ordenada = selection_sort(lista)
print("Lista ordenada:", lista_ordenada)
