contador = 0
faznada = 0
for num in range(2,101):
    if num  == 2 or num  == 3 or num == 5 or num == 7:
        contador += 1
    elif not num  % 2 == 0 and not num % 3 == 0 and not num % 5 == 0 and not num % 7 == 0:
        contador += 1
        # print(f'{num} é um número primo')
print(f'Há {contador} números primos entre 1 e 100')

