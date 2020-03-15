lista =  [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]
times = []

for partida in lista:
    time1, time2, faltas = partida[0], partida[1], partida[2]

    if time1 in times:
        i = 1
        for nome in times:
            if nome == time1:
                times[i] += faltas[0]
            i += 1
    else:
        times.append(time1)
        times.append(faltas[0])

    if time2 in times:
        i = 1
        for nome in times:
            if nome == time2:
                times[i] += faltas[1]
            i += 1
    else:
        times.append(time2)
        times.append(faltas[1])

#total de faltas do campeonato
print(sum(times[1::2]))

#o time que fez mais faltas
maior, menor, i = 0, 1000, 0
paisMenor, paisMaior = '', ''
for val in times:
    if(type(val) == type(1)):
        if val < menor:
            menor = val
            paisMenor = times[i-1]
        if val > maior:
            maior = val
            paisMaior = times[i-1]
    i += 1
    
print('Time com mais faltas:', paisMaior)
print('Time com menos faltas:', paisMenor)

#o time que fez menos faltas