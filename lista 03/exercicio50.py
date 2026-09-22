valor = float(input('Digite o valor desta compra: R$'))
soma = 0
total = 0
while valor != -1:
    soma += valor
    print(f'O valor atual do carrinho é de R${soma:.2f}')
    print('-' * 15)
    valor = float(input('Digite o valor desta nova compra: R$'))
if soma >= 250:
    print('Você adquiriu 10% de desconto')
    total = soma * .9 
elif soma >= 100:
    print('Você adquiriu 5% de desconto')
    total = soma * .95 
print(f'O valor total do carrinho é de R${total:.2f}')