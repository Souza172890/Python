num = int(input('Digite um valor: '))
tot = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO valor {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso é um número PRIMO! ')
else:
    print('E por isso NÃO é um número PRIMO')