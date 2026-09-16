print('Verificando múltiplos de 3 e de 5')
print('---------------------------------')
for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} é múltiplo de 3 e de 5')
    elif i % 3 == 0:
        print(f'{i} é múltiplo de 3')
    elif i % 5 == 0:
        print(f'{i} é múltiplo de 5')
    else:
        print(f'{i} não é múltiplo de nenhum dos dois')