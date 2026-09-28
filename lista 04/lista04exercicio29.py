def classificar_nota(nota):
    if nota >= 9:
        return 'A'
    elif nota >= 7:
        return 'B'
    elif nota >= 5:
        return 'C'
    elif nota < 5:
        return 'D'
nota=int(input('Digite a nota do aluno: '))
print(f'O conceito final do aluno é {classificar_nota(nota)}')