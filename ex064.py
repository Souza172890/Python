num = 0
cont = 0
soma = 0
num = int(input('Digite um número ou 999 para parar: '))
#os termos acima podem ser escritos: num = cont = soma = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número ou 999 para parar: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
