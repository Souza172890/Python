from datetime import date
ano = int(input('Digite o ano que quer analisar, ou digite 0 para saber se o ano atual é bissexto '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano é Bissexto')
else:
    print('Esse ano não é Bissexto')


