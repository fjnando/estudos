menu = '''
...Escolha uma opção...
[d] deposito
[s] saque
[e] extrato
[q] sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input(f'informe o valor do deposito: '))
        print(f'\ndeposito realizado com sucesso no valor de R$ {valor:.2f}')
        
        if valor > 0:
            saldo += valor
            extrato += f'deposito: R$ {valor:.2f}\n'
            

        else:
            print('Operacao falhou: o valor informado é invalido')


    elif opcao == 's':
        valor = float (input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print('Operação falhou: Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou: O valor do saque excede o limite. ')

        elif excedeu_saques:
            print('Operação falhou: Número máximo de saques excedido. ')

        elif valor > 0:
            saldo -= valor
            extrato += f'saque: R$ {valor:.2f}\n'
            numero_saques +=1
            print(f'\nsaque realizado com sucesso no valor de R$ {valor:.2f}')

        else:
            print('Operação falhou: O valor informado é invalido. ')

    elif opcao == 'e':
        print('\n.............. Extrato ....................')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nsaldo: R$ {saldo:.2f}')
        print('.............................................')
    
    elif opcao == 'q':
        print('Obrigado por utilizar os nossos serviços')
        print('')
        break


    else:
        print('operação invalida, por favor selecione somente a operação desejada') 