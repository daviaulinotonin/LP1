idade = int(input('Informe a idade desta pessoa '))
while idade >-1:
    if idade >=18:
        print('Maior de idade')
        idade = int(input('Informe a idade desta pessoa '))
    else:
        print('Menor de idade')
        idade = int(input('Informe a idade desta pessoa '))