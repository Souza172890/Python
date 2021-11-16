velocidade = float(input('Qual a velocidade do carro? '))
if velocidade >80:
    print('Multado, você ultrassou a velocidade limite que é 80km/h')
    multa = (velocidade - 80)*7
    print('Você deve pagar uma multa de R${:.1f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')
