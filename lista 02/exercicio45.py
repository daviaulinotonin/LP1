salario = float(input('Informe seu salário R$ '))
tempo = int(input('Informe em anos quanto tempo você tem de empresa '))
if salario < 2000:
  if tempo >= 5:
    print('Elegível a reajuste')
  else:
    print('Não elegível a reajuste')
else:
  print('Não elegível a reajuste')