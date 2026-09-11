print('Você já é sócio da loja? ')
socio = input('S/N ')

if socio.capitalize() == 'S':
  print('O preço do ingresso para sócios é de R$20,00')
else:
  print('O preço do ingresso para não sócios é de R$40,00')