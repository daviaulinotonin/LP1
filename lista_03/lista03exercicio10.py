# cont = 0
# while True:
#   num = int(input('Digite um número '))
#   if num <0:
#     break
#   cont += 1
# print(f'{cont} números positivos foram digitados')

num = int(input('Digite um número '))
cont = 0
while True:
  cont += 1
  num = int(input('Digite um número '))
  if num <0:
    break
print(f'{cont} números positivos foram digitados')