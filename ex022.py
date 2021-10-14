nome = str(input('Qual o seu nome completo? ')).strip()
print('Analisando o seu nome...')
print('O seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('O seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('O seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))



