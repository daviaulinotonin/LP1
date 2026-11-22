ano = int(input('Informe um ano a ser calculado '))
print(ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))