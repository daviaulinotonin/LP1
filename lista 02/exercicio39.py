peso = int(input('Informe o seu peso em kg '))
altura = int(input('Informe sua altura em cm '))
imc = peso/((altura/100)**2)
print('Seu IMC é', imc)
if imc < 18.5:
  print('Você está abaixo do peso')
elif imc < 25:
  print('Você está com o peso normal')
elif imc < 30:
  print('Você está com sobrepeso')
else:
  print('Você está obeso')