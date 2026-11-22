password = 'fatec123'
cont = 3
senha = input('Digite a senha \n >')
while senha != password:
    cont -= 1
    if cont == 2:
        senha = input(f'Senha incorreta. \nVocê tem mais {cont} tentativas \n >')
    elif cont == 1:
        senha = input(f'Senha incorreta. \nVocê tem mais {cont} tentativa \n >')
    elif cont == 0:
        print('Acesso negado')
        break
    1
    print('Acesso liberado')
