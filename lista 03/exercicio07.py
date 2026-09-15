password = 'fatec123'
senha = input('Digite a senha ')
while True:
  if senha == password:
    print('Acesso liberado')
    break
  senha = input('Senha incorreta. Tente novamente ')