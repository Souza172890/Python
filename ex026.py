frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra a aparece {} vezes na frase;'.format(frase.count(A)))
print('A primeira letra a, apareceu na posição {};'.format(frase.find(A)+1))
print('A ultima letra a, aparece na posição {}'.format(frase.rfind(A)+1))


