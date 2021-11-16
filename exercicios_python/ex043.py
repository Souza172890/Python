peso = float(input('Digite o seu peso: '))
altura = float(input('Agora digite a sua altura: '))
imc = (peso/(altura**2))
print('O valor do seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Parabéns, você está com Peso Ideal!')
elif imc >= 25 and imc < 30:
    print('Alerta, você está Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Cuidado, você está em Obesidade')
else:
    print('Você está em Obesidade Mórbita')