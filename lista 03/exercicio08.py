num = int(input('Digite um número positivo '))
dig = 0
while num != 0:
  num//=10
  # precisa estar como // para poder arredondar o resultado da divisão
  dig += 1
print(f'Este número possui {dig} digitos')