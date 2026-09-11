idade = int(input('Informe sua idade '))
print('Informe seu sexo')
sexo = input('Digite F para feminino e M para masculino ')
# if sexo.capitalize() == 'M' and idade >=18:
  # print('Apto ao serviço militar')
if sexo.capitalize() == 'M':
  if idade >=18:
    print('Apto ao serviço militar')
  else:
    print('Inapto ao serviço militar')
else:
  print('Inapto ao serviço militar')