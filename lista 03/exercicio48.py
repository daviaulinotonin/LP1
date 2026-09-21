ingressos = 5
comprados = 0
sistema = int(input("Deseja iniciar a compra?\n1 - Sim \n2 - Não\n> "))
while sistema >2:
    print('Opção inválida.')
    print('-'*15)
    sistema = int(input('Deseja tentar novamente?\n1 - Sim \n2 - Não\n'))
while sistema == 1:
    print(f'Ingressos disponíveis: {ingressos}')
    qnt = int(input('Quantos ingressos deseja comprar?\n> '))
    if qnt > ingressos:
        qnt = 0
        print('Não é possível comprar mais ingressos que o número disponível.')
        print('-'*15)
        sistema = int(input('Deseja tentar novamente?\n1 - Sim \n2 - Não\n'))
        continue
    print(f'Você comprou {qnt} ingresso(s).')
    print('-'*15)
    ingressos -= qnt
    print(f'Ingressos disponíveis: {ingressos}')
    if ingressos == 0:
        print('Os ingressos para está obra acabaram.')
        break
    sistema = int(input('Deseja comprar mais ingressos?\n1 - Sim \n2 - Não\n'))
print('Sistema finalizado.')


                    


# sistema = int(input("Deseja realizar mais uma compra?\n1 - Sim \n2 - Não\n> "))
                
# elif sistema == 2:
# print('Sistema finalizado.')
# break
# qnt = int(input('Quantos ingressos deseja comprar?\n> '))