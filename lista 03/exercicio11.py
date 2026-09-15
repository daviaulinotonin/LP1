num = int(input('Digite um número maior que 1 '))
while num !=1:
    if not num  == 2 and num % 2 == 0 or not num  == 3 and num % 3 == 0 or not num == 5 and num % 5 == 0:
        print(f'{num} não é um número primo')
    # if not num  == 3 and num % 3 == 0:
    #     print(f'{num} não é um número primo')
    else:
        print(f'{num} é um número primo')
    break

# como fazer sem IF?