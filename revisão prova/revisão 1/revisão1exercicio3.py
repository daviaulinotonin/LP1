alunos = int(input('Informe quantos alunos estão nesta turma: '))
aprovados = 0
recuperacao = 0
reprovados = 0
media_geral = 0
for aluno in range(alunos):
    nome = input('Digite o nome do aluno: ')
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1+n2)/2
    media_geral+=media

    if media >= 6:
        status = 'Aprovado'
        aprovados += 1

    elif media > 4:
        status = 'Recuperação'
        recuperacao += 1

    else:
        status = 'Reprovado'
        reprovados += 1
    media_geral=
    print(nome.capitalize())
    print(f'Média: {media}')
    print(f'Situação: {status}')
print(15*'-')
print(f'{aprovados} alunos aprovados')
print(f'{recuperacao} alunos em recuperação')
print(f'{reprovados} alunos reprovados')
print(f'{media_geral} é a média geral desta turma')
