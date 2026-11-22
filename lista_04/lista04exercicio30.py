def imprime_triangulo(linhas):
    for i in range(1, linhas + 1):
        print('*'*i)
linhas=int(input('Quantas linhas você quer que seja impresso? '))
imprime_triangulo(linhas)