senha = input('Digite a senha ')

correta = 'fatec123'

while senha != correta:
    print('Senha incorreta.')
    senha = input('Tente novamente ')
print('Acesso liberado')