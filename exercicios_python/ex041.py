from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade <= 9:
    print('Participante categoria MIRIM')
elif idade >= 10 and idade <= 14:
    print('Participante categoria INFANTIL')
elif idade >= 14 and idade <= 19:
    print('Participante categoria JÚNIOR')
elif idade >= 20 and idade <= 25:
    print('Participante SÊNIOR')
else:
    print('Participante categoria MASTER')