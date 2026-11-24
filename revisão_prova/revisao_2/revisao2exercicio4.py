# O serviço de saneamento de um município deseja calcular a conta de água de seus clientes. O
# valor depende do consumo mensal em metros cúbicos (m³), conforme a tabela abaixo:
# Faixa de Consumo (m³) Cobrança
# Até 10 Valor fixo de R$ 35,00
# De 11 até 20 R$ 5,20 por m³
# De 21 até 50 R$ 7,80 por m³
# Acima de 50 R$ 10,50 por m³
# Além da água, é cobrada a tarifa de esgoto, que corresponde a 80% do valor da água. Os cálculos
# devem seguir as fórmulas:
# Valor da Água = Consumo x Valor por m³ (ou R$ 35,00 na primeira faixa)
# Valor do Esgoto = Valor da Água x 0,80
# Total = Valor da Água + Valor do Esgoto
# Faça um programa que solicite o consumo do mês, identifique a faixa aplicável e exiba o valor da
# água, o valor do esgoto e o total da conta. Caso o consumo informado seja negativo, exiba a
# mensagem "Consumo inválido!".
consumo = int(input('Informe o consumo de água (em m³)\n>'))
if consumo < 0:
    print('Quantidade inválida.')
else:
    if consumo <= 10:
        agua = 35
    elif consumo <=20:
        agua = consumo * 5.2
    elif consumo <= 50:
        agua = consumo * 7.8
    else:
        agua = consumo * 10.5
    print(f'O valor da água com consumo de {consumo} m³ é R${agua:.2f}')
    esgoto = agua * 0.80
    print(f'O valor do esgoto é de R${esgoto:.2f}')
    total = agua + esgoto
    print(f'O total da conta de saneamento é de R${total:.2f}')