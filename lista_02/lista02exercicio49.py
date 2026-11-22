temp = int(input('Informe a temperatura atual '))
umid = int(input('Informe a umidade atual '))

if temp >30:
  if umid <30:
    print('Risco de incêndio!')
  else:
    print('Calor, mas sem risco de incêndio.')