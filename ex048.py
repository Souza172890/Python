cont = 0
soma = 0
for c in range (1,501,2):
    if c % 3 == 0:
        cont = cont + 1  #outra forma --> cont += c
        soma = soma + c  #outra forma --> soma += 1
print('A soma dos {} solicitados é {}'.format(cont, soma))