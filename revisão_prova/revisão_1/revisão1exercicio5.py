carro = 0
moto = 0
veiculos = 0
gratuito = 0
lucro_total = 0

qnt_veiculos = int(input('Quantidade de veículos: '))
for veiculo in range(qnt_veiculos):
    placa = input('Placa: ')
    tipo = input('Carro - C \nou \nMoto - M\n> ').upper()

    if tipo == 'C':
        carro += 1
        primeira_hora = 8
        hora_adicional = 4
            
    elif tipo == 'M':
        moto += 1
        primeira_hora = 4
        hora_adicional = 2

    else:
        print('Tipo inválido!')
        continue

    veiculos += 1
    minutos = int(input('Digite o tempo de permânencia em minutos: '))
    if minutos <= 15:
        gratuito += 1
        horas = 0
        valor = 0
        print(f'Placa: {placa} - Isento\n')

    else:
        horas = minutos // 60
        if minutos % 60 > 0:
            horas += 1
        valor = primeira_hora + (horas - 1) * hora_adicional
        print(f'Placa: {placa} - Horas cobradas: {horas} - Valor: R${valor:.2f}\n')
        lucro_total += valor

print(f'{veiculos} veículos processados: {carro} carros e {moto} motos')
print(f'{gratuito} gratuitos')
print(f'Total arrecadado R${lucro_total:.2f}')