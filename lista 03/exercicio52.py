estoque = 100
comprados = 0
sistema = int(input("Deseja iniciar a compra?\n1 - Sim \n2 - Não\n> "))
while True:
    if sistema == 1:
        print(f'Unidades disponíveis: {estoque}')
        qnt = int(input('Quantas unidades deseja comprar?\n> '))
        if qnt > estoque:
            qnt = 0
            print('Não é possível comprar mais unidades que o número disponível.')
            print('-'*15)
            sistema = int(input('Deseja tentar novamente?\n1 - Sim \n2 - Não\n'))
            continue
        print(f'Você comprou {qnt} unidade(s).')
        print('-'*15)
        estoque -= qnt
        print(f'Unidades disponíveis: {estoque}')
        if estoque == 0:
            print('As unidades em estoque acabaram.')
            break
        sistema = int(input('Deseja comprar mais unidades?\n1 - Sim \n2 - Não\n'))
    elif sistema != 1 and sistema != 2:
        print('Opção inválida.')
        print('-'*15)
        sistema = int(input('Deseja tentar novamente?\n1 - Sim \n2 - Não\n'))
    elif sistema == 2:
        break
print('Sistema finalizado.')