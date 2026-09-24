def exibir_nome(nome):
    print(f'Seja bem-vindo {nome}!')
nome=input('Digite seu nome: ') #input não pode ficar dentro da função
exibir_nome(nome.capitalize())
