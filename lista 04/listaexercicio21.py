def saudacao_personalizada(nome,saudacao='Olá'):
    print(f'{nome}!')
    
nome=input('Digite seu nome: ')
saudacao_personalizada(nome.capitalize())
saudacao_personalizada( nome.capitalize())