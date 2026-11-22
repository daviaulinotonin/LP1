pos = 0
neg = 0
num = int(input('Digite um número '))
while num != 0:
    if num > 0:
        pos += 1
        num = int(input('Digite outro número '))
    elif num < 0:
        neg += 1
        num = int(input('Digite outro número '))
print(f'No total, foram digitados {pos} números positivos e {neg} números negativos.')
