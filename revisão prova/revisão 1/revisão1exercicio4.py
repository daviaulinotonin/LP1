leitura_anterior = int(input('Informe a leitura anterior: '))
leitura_atual = int(input('Informe a leitura atual: '))
if leitura_atual < leitura_anterior:
    print('Leitura inválida!')
consumo = leitura_atual - leitura_anterior
tarifa = 0

if consumo > 400:
    tarifa = 1.10
elif consumo > 201:
    tarifa = 0.90
elif consumo > 101:
    tarifa = 0.75
else:
    tarifa = 0.60

valor_consumo = consumo * tarifa
print(valor_consumo)
percentual = 0
bandeira = input('Informe a bandeira \nV - Verde \nA - Amarela\nR - Vermelha\n> ')
if not bandeira == 'v' and not bandeira == 'a' and not bandeira == 'r':
    print('Bandeira inválida!')

if bandeira == 'v':
    percentual = 0
elif bandeira == 'a':
    percentual = .05
elif bandeira == 'r':
    percentual = .10

acrescimo = valor_consumo * percentual
total =  valor_consumo + acrescimo + 12
print(total)