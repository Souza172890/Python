dist = float(input('Digite a distância de sua viajem: '))
if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print('O preço da passagem será de R$ {:.2f}.'.format(preço))