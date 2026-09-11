print('Informe um mês do ano para verificar a estação do respectivo trimestre ')
print('1- Janeiro\n2 - Fevereiro\n3- Março\n4- Abril\n5- Maio\n6- Junho\n7- Julho\n8- Agosto\n9- Setembro\n10- Outubro\n11- Novembro\n12- Dezembro')
mes = int(input( ))
if mes <=3:
  print('A estação desse trimestre é o Verão')
elif mes <=6:
  print('A estação desse trimestre é o Outono')
elif mes <=9:
  print('A estação desse trimestre é o Inverno')
elif mes <=12:
  print('A estação desse trimestre é a Primavera')