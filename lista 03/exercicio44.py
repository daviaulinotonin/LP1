temp = int(input(f'Digite a temperatura em Cº:'))
while temp >-100:
    if temp >= 30:
        print('A temperatura está muito quente')
        temp = int(input(f'Digite a temperatura em Cº:'))
    elif temp >=18:
        print('A temperatura está agradável')
        temp = int(input(f'Digite a temperatura em Cº:'))
    elif temp >=0:
        print('A temperatura está fria')
        temp = int(input(f'Digite a temperatura em Cº:'))
    else:
        print('A temperatura está congelante')
        temp = int(input(f'Digite a temperatura em Cº:'))