cpu = 42
soma = 0
jogar = int(input('Deseja jogar Par ou Ímpar?\n1 - Sim\n2 - Não\n> '))
while True:
    if jogar == 1:
        # par_ou_impar = str(input('Legal!\nVocê escolhe par ou impar?\n'))
        # if par_ou_impar.lower == 'par':
        par_ou_impar = int(input('Legal!\nVocê escolhe\n1 - Par\n ou\n2 - Ímpar?\n'))

        if par_ou_impar == 1: #escolher PAR
            print('OK, eu vou ser ímpar então!')
            num = int(input('Digite um número\n> '))
            if num <0:
                print('O número não pode ser negativo')
                num = int(input('Digite outro número\n> '))
            soma = num + cpu
            print(f'Ok, {num} mais {cpu} fica...{soma}!')

            if soma % 2 == 0:
                print(f'{soma} é par! Você ganhou!')
                jogar = int(input('Deseja jogar novamente?\n1 - Sim\n2 - Não\n> '))

            else:
                print(f'{soma} é ímpar! Eu ganhei!')
                jogar = int(input('Deseja jogar novamente?\n1 - Sim\n2 - Não\n> '))

        elif par_ou_impar == 2: #escolher IMPAR
            print('OK, eu vou ser par então!')
            num = int(input('Digite um número\n> '))
            if num <0:
                            print('O número não pode ser negativo')
                            num = int(input('Digite outro número\n> '))
            soma = num + cpu
            print(f'Ok, {num} mais {cpu} fica...{soma}!')    

            if soma % 2 == 0:
                print(f'{soma} é par! Eu ganhei!')
                jogar = int(input('Deseja jogar novamente?\n1 - Sim\n2 - Não\n> '))

            else:
                print(f'{soma} é ímpar! Você ganhou!')
                jogar = int(input('Deseja jogar novamente?\n1 - Sim\n2 - Não\n> '))
    elif jogar == 2:
        print('Tudo bem...')
        break  
    elif jogar != 1 and jogar != 2:
        print('Opção inválida.')
        print('-'*15)
        sistema = int(input('Deseja tentar novamente?\n1 - Sim \n2 - Não\n> '))
