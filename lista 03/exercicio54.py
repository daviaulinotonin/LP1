num = int(input('Digite um número '))
while not num >=1 or not num <=10:
    print(f'{num} não faz parte do conjunto desejado')
    print('Tente novamente')
    num = int(input('Digite outro número '))
print('OK')