def imprime_triangulo(linhas):
    for n in linhas:
        print('*'*n)

linhas=int(input('Quantas linhas você quer que seja impresso? '))
print(imprime_triangulo(linhas))