minutos = int(input('Informe a quantidade de minutos utilizados neste mês '))
if minutos <= 100:
  print('O valor total deste mês é de R$' , minutos*.25)
elif minutos <=300:
  print('O valor total deste mês é de R$' , minutos*.20)
elif minutos <=500:
  print('O valor total deste mês é de R$' , minutos*.15)
else:
  print('O valor total deste mês é de R$' ,  minutos*.10)