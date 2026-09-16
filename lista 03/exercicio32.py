num = int(input('Digite um número '))
while True:
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é ímpar')
    num = int(input('Digite um número '))
    if num == 0:
        break
