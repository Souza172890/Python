num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
if num1 > num2:
    print('O primeiro número é maior!')
elif num2 > num1:
    print('O segundo número é maior!')
elif num1 == num2 or num2 == num1:
    print('Não existe valor maior, os dois são iguais!')