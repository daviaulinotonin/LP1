def media_ponderada(n1,n2,n3):
    media = (n1 * 2 + n2 * 3 + n3 * 5) / (2 + 3 + 5)
    print(f'A média final do aluno é {media}')
    if media >=8:
        return(f'Conceito final: A')
    elif media >=7:
        return(f'Conceito final: B')
    elif media >=6:
        return(f'Conceito final: C')
    elif media >=5:
        return(f'Conceito final: D')
    else:
        return(f'Conceito final: E')
n1 = float(input('Digite a nota do Trabalho de Laboratório: '))
n2 = float(input('Digite a nota da Avaliação Semestral: '))
n3 = float(input('Digite a nota do Exame Final: '))
print(media_ponderada(n1,n2,n3))
