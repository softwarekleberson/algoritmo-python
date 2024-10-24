def ordenacao(arr):
    for i in range(len(arr)):
        menor = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[menor]:
                menor = j
        
        arr[i], arr[menor] = arr[menor], arr[i]
    
    return arr

numeros = [1,2,5,4,9,7,10,20,15]
print("Ordenados:", ordenacao(numeros))