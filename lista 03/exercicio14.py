num = int(input('Digite um número positivo '))
soma = 0
while num > 0:
    dig = num%10
    
    quo = num//10
    num = quo
    soma += dig
print(f'A soma dos dígitos do número digitado é de {soma}')