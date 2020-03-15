def tem_33(lista):
  seq = False

  for val in lista:
    if val == 3:
      if seq == True:
        return True
      seq = True
    else:
      seq = False

print('True' if tem_33([3,1,3,3]) == True else 'False')