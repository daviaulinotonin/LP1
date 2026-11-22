valor = float(input('Informe o valor da compra '))
if valor >= 100:
  print('Devido o desconto de 10%, o custo final é de R$' , valor * .9)
else:
  print('O custo final é de R$' , valor)
