a = [1,2,3,4,5,6,7]
b = [1,2,3,4,5,6,7]

for i in range(len(a)):
    if b[i] == a[i]:
        continue
    else:
        print('Listas diferentes')
        exit()
print('Listas iguais')