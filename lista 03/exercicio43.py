for i in range(11):
    nota_aluno = int(input('Digite a nota do aluno '))
    if nota_aluno >= 9:
        print('Conceito final: A\n----------')
    elif nota_aluno >= 7:
        print('Conceito final: B\n----------')
    elif nota_aluno >= 5:
        print('Conceito final: C\n----------')
    else:
        print('Conceito final: D\n----------')
print('Notas inseridas em sistema.\n----------')
