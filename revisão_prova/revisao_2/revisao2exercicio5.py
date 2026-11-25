# Uma loja paga a seus vendedores um salário fixo de R$ 1.800,00 mais uma comissão sobre o
# total vendido no mês. O percentual de comissão depende da faixa de vendas:
# Total Vendido no Mês (R$) Comissão (%) Bônus (R$)
# Até 5.000,00 3% 0,00
# De 5.000,01 até 10.000,00 5% 0,00
# De 10.000,01 até 20.000,00 7% 0,00
# Acima de 20.000,00 9% 500,00
# Os cálculos devem seguir as fórmulas:
# Comissão = Total Vendido x Percentual de Comissão
# Salário Final = 1.800,00 + Comissão + Bônus
# Faça um programa que:
# • Solicite a quantidade de vendedores.
# • Para cada vendedor, leia o nome e o total vendido no mês.
# • Calcule e exiba o nome, a comissão e o salário final do vendedor.
# • Caso o total vendido seja negativo, exiba a mensagem "Valor inválido!" e não inclua esse
# vendedor nos cálculos.
# • No final, exiba o total pago pela loja (soma dos salários finais) e o nome do vendedor com o
# maior salário final.
melhor_vendedor = ''
maior_salario = 0
total = 0
fixo = 1800

vendedores  = int(input('Informe a quantidade de vendedores: '))
if vendedores <= 0:
    print('Programa encerrado.')
else:
    for vendedor in range(1, vendedores + 1):
        nome = input('Digite o nome do vendedor: ')
        vendas = int(input('Quantidade vendida: '))
        if vendas <0:
            print('Valor inválido.')
            continue
        elif vendas <= 5000:
            perc = 0.30
            bonus = 0
        elif vendas <= 10000:
            perc = 0.50
            bonus= 0
        elif vendas <= 20000:
            perc = 0.70
            bonus = 0
        else:
            perc = 0.90
            bonus = 500
        comissao = vendas * perc
        salario = fixo + comissao + bonus
        total += salario
        if salario > maior_salario:
            melhor_vendedor = nome
            maior_salario = salario
        print(f'Vendedor: {nome} | Comissão: R${comissao:.2f} | Salário: R${salario:.2f}\n')
    print(f'Total a ser pago: R${total:.2f}')
    print(f'Melhor vendedor: {melhor_vendedor} | Salário: R${maior_salario:.2f}')