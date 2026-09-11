ano = int(input('Informe um ano a ser calculado '))
if ano % 400 == 0:
  print(f'{ano} é um ano bissexto.')
elif ano % 100 != 0:
    if ano % 4 == 0:
      print(f'{ano} é um ano bissexto.')
    else:
      print(f'{ano} não é um ano bissexto')
else:
  print(f'{ano} não é um ano bissexto')