soma = 0
while True:
  num = int(input('Digite um número '))
  soma += num
  if num == 0:
    print(f'A soma dos números digitados é {soma}')
    break
