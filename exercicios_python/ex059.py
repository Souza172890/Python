n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 * n2
        print('A multiplicação de {} x {} = {}'.format(n1,n2,produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é: '.format(n1,n2,maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
print('Fim do Programa! Volte Sempre!')