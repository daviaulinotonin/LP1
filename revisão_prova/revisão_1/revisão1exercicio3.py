alunos = int(input('Informe quantos alunos estão nesta turma: '))
aprovados = 0
recuperacao = 0
reprovados = 0
nota_geral = 0
for aluno in range(alunos):
    nome = input('Digite o nome do aluno: ')
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1+n2)/2
    nota_geral+=media

    if media >= 6:
        status = 'Aprovado'
        aprovados += 1

    elif media > 4:
        status = 'Recuperação'
        recuperacao += 1

    else:
        status = 'Reprovado'
        reprovados += 1
    print(nome.capitalize())
    print(f'Média: {media}')
    print(f'Situação: {status}')
print(15*'-')
media_geral=nota_geral/alunos
print(f'{aprovados} alunos aprovados')
print(f'{recuperacao} alunos em recuperação')
print(f'{reprovados} alunos reprovados')
print(f'A média geral desta turma é {media_geral}')
