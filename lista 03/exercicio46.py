idade = int(input('Digite uma idade '))
crianca = 0
adolescente = 0
adulto = 0
idoso = 0
while idade>0:
    if idade <12:
        crianca+=1
        idade = int(input('Digite outra idade '))
    elif idade <18:
        adolescente+=1
        idade = int(input('Digite outra idade '))
    elif idade <60:
        adulto+=1
        idade = int(input('Digite outra idade '))
    else:
        idoso+=1
        idade = int(input('Digite outra idade '))
print(f'No total, são {crianca} crianças, {adolescente} adolescentes, {adulto} adultos e {idoso} idosos')        