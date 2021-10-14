a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#verificando o menor valor:
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando o maior:
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O valor maior é {} e o menor é {}'.format(maior,menor))

