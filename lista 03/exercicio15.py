num = int(input('Digite o valor a ser depositado R$'))
saldo = 0   
while num != 0:
    saldo +=num
    num = int(input('Digite o valor a ser depositado R$'))
print(f'O saldo é de R${saldo}')