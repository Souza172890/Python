n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nova: '))
média = (n1 + n2) / 2
if média >= 7.0:
    print('Aluno com média {}, aluno APROVADO'.format(média))
elif média < 5.0:
    print('Aluno com média {}, aluno REPROVADO!'.format(média))
else:
    print('Aluno com média {}, aluno em RECUPERAÇÃO'.format(média))



