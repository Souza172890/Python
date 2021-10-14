valor = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
anos = int(input('Em quantos anos deseja pagar o financiamento? '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
print('Para financiar uma casa de R$ {:.2f} em {} anos'.format(valor,anos), end = '')
print(' a prestação será de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo Aprovado')
else:
    print('Empréstimo Negado')

