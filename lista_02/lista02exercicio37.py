idade = int(input('Informe sua idade '))
if idade <12:
  print('Faixa etária: Criança')
elif idade <18:
  print('Faixa etária: Adolescente')
elif idade <60:
  print('Faixa etária: Adulto')
else:
  print('Faixa etária: Idoso')