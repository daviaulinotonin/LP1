valor_venal = float(input('Informe o valor venal do imóvel: R$'))

if valor_venal <= 100000:
    print('Não há IPTU a ser pago nesta faixa.')

elif valor_venal <= 250000:
    valor_total = (valor_venal * .05) - 500
    print(f'O valor total a ser pago é de R${valor_total}')

elif valor_venal <= 500000:
    valor_total = (valor_venal * .1) - 1750
    print(f'O valor total a ser pago é de R${valor_total}')

elif valor_venal <= 1000000:
    valor_total = (valor_venal * .15) - 4250
    print(f'O valor total a ser pago é de R${valor_total}')

elif valor_venal > 1000000:
    valor_total = (valor_venal * .2) - 9250
    print(f'O valor total a ser pago é de R${valor_total}')
