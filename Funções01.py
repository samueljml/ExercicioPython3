def espiao(lista):
  seq = [0, 0, 7]
  j = 0
  for i in range(0, len(lista)):

    if seq[j] == lista[i]:
      j += 1
      if j == 3:
        return True
  return False

Lista = [1,2,4,0,0,7,5]
print('True' if espiao(Lista) == True else 'False')