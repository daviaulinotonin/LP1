saldo = 0
deposito = 0
saque = 0
depositar = 1
sacar = 2
sair = 3
opcao = int(input('Selecione qual operação deseja realizar:\n1 - Depósito\n2 - Saque\n3 - Sair\n> '))
while True:
    if opcao == 1:
        deposito = float(input('Informe o valor que deseja depositar:\nR$'))
        saldo += deposito
        print(f'Depósito de R${deposito:.2f} realizado com sucesso.')
        print(f'---------------\nSaldo atual: R${saldo:.2f}\n---------------')
        opcao = int(input('Selecione qual operação deseja realizar:\n1 - Depósito\n2 - Saque\n3 - Sair\n> '))   

    elif opcao == 2:
        if saldo == 0:
            print('Não há saldo disponível para sacar dinheiro.\n---------------')
            opcao = int(input('Selecione qual operação deseja realizar:\n1 - Depósito\n2 - Saque\n3 - Sair\n> '))

        saque = float(input('Informe o valor que deseja sacar:\nR$'))
        if saldo - saque < 0:
            print('Não é possível sacar um valor maior que o disponível em conta.\n---------------')
            opcao = int(input('Selecione qual operação deseja realizar:\n1 - Depósito\n2 - Saque\n3 - Sair\n> '))
        
        else:
            saldo -= saque
            print(f'Saque de R${saque:.2f} realizado com sucesso.')
            print(f'---------------\nSaldo atual: R${saldo:.2f}\n---------------')
            opcao = int(input('Selecione qual operação deseja realizar:\n1 - Depósito\n2 - Saque\n3 - Sair\n> '))
        
    elif opcao == 3:
        print('Operação finalizada.\n---------------')
        break
    elif opcao >3:
        print('Opção inválida.')
        opcao = int(input('Selecione qual operação deseja realizar:\n1 - Depósito\n2 - Saque\n3 - Sair\n> '))