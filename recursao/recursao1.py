def imprime(i):
    if i == 0:
        return
    
    else:
        imprime(i-1)
        print('valor de i:', i)

imprime(5)
