print('Olá!')
nome = input('Qual o seu nome? ')
print('Bem vindo ' + nome.capitalize() + '!')
idade = int(input('Qual a sua idade? '))
if idade >= 30:
    print('Tá véio hein?')
else:
    print('Nossa, que novinho...')
cor = input('Qual sua cor favorita? ')
if cor.capitalize() == 'Rosa':
    print('Roooosa ' + nome.capitalize() +'?')
else:
    print('Legal')