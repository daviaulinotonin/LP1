def saudacao_personalizada(nome , saudacao='Olá'):
    '''
    saudacao está definida por padrão para Olá, a não ser que outro parâmetro seja inserido
    '''
    print(f'{saudacao}, {nome}!')
    
nome=input('Digite seu nome: ')
saudacao_personalizada(nome.capitalize())
saudacao_personalizada(nome.capitalize(), 'Bem-vindo')