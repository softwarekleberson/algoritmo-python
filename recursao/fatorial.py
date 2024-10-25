def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x-1)

fat = fatorial(4)
print(fat)