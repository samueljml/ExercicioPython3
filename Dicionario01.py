quantidade_de_voltas = 3
quantidade_de_corredores = 2

def lerVolta():
    a = []
    for i in range(quantidade_de_voltas):
        a.append(int(input()))
    return a

# Lendo os valores dos corredores
d = {}
while quantidade_de_corredores > 0:
  nome = input('Digite o nome do corredor:')
  d[nome] = lerVolta()
  quantidade_de_corredores -= 1

# Calculando os intervalos
intervalo, nomes, i = [], [], 0
menor = [10000, 0, '']
print(menor[0])
for jogador in d:
  aux = []
  for i in range(len(d[jogador])):
    if i != 0:
      if menor[0] > d[jogador][i] - d[jogador][i-1]:
        menor[0] = d[jogador][i] - d[jogador][i-1]
        menor[1] = i+1
        menor[2] = jogador
      aux.append(d[jogador][i] - d[jogador][i-1]) 
  i += 1
  intervalo += [aux]
  nomes.append(jogador)

print('\nDados melhor volta: ')
print('- Corredor:', menor[2])
print('- Volta:', menor[1])
print('- Tempo:', menor[0], 'segundos\n')

#Melhor corredor:
print('Melhor tempos:')
total = []
i = 0
for interv in intervalo:
  total.append([sum(interv), nomes[i]])
  i+= 1

total.sort()
for corredores in total:
  print(corredores[1], ':', corredores[0], 'segundos')