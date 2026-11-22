valor = float(input('Informe o valor da compra '))
if valor <=50:
  print('O custo final é de R$' , valor)
elif valor <=200:
    print('Devido o desconto de 5%, o custo final é de R$' , valor * .95)
elif valor <=500:
    print('Devido o desconto de 10%, o custo final é de R$' , valor * .9)
else:
  print('Devido o desconto de 15%, o custo final é de R$' , valor * .85)
