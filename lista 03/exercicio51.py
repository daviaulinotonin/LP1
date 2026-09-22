contador = 0
faznada = 0
for num in range(2,101):
    # if not num  == 2 and num % 2 == 0 or not num  == 3 and num % 3 == 0 or not num == 5 and num % 5 == 0 or not num == 7 and num % 7 == 0:
        # faznada += 1
        # print(f'{num} não é um número primo')
    # else:
    if num  == 2 or num  == 3 or num == 5 or num == 7:
        contador += 1
        if not num  % 2 == 0 or not num % 3 == 0 or not num % 5 == 0 or not num % 7 == 0:
                    contador += 1
        # print(f'{num} é um número primo')
print(f'Há {contador} números primos entre 1 e 100')

