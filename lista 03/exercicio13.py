soma = 0
cont = 0
media = 0
while True:
    nota = int(input('Digite a nota do aluno '))
    if nota == -1:
        media = soma/cont
        print(f'A média da sala é de {media}')
        break
    cont += 1
    soma += nota
