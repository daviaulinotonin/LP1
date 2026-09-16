num = 42
chute = int(input('Tente acertar o número secreto '))
while chute != num:
    if chute<0:
        print('O número secreto não é negativo')
        chute = int(input('Chute outro número '))
    elif chute<num:
        print(f'{chute} é MENOR que o número secreto')
        chute = int(input('Chute outro número '))
    elif chute>num:
        print(f'{chute} é MAIOR que o número secreto')
        chute = int(input('Chute outro número '))
print('Parabéns! Você acertou!')