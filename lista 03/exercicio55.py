contador = 0
for dias in range(1,8):
    temp = int(input(f'Informe a temperatura do {dias}º da semana: '))
    if temp >30:
        contador+=1
if contador == 0:
    print('Nenhum dia nesta semana teve temperatura superior a 30ºC')
elif contador == 1:
    print('Somente 1 dia nesta semana teve temperatura superior a 30ºC')
elif contador == 7:
    print('Todos os dias nesta semana tiveram temperatura superior a 30ºC')
else:
    print(f'{contador} dias nesta semana tiveram temperatura superior a 30ºC')