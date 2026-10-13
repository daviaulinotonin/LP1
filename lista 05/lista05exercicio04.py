def confere_idade(idade):
    if idade <14:
        return ('Não pode entrar.')
    elif idade <18:
        return ('Pode entrar acompanhado dos pais, não pode beber')
    elif idade >=18:
        return ('Pode entrar, pode beber')
idade = int(input('Digite a idade: '))
print(confere_idade(idade))