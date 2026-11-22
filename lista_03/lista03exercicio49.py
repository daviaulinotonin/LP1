num = int(input('Digite um número '))
maior = num
menor = num
if num>maior:
    maior = num
elif num<menor:
    menor = num
for i in range(9):
    num = int(input('Digite outro número '))
    if num>maior:
        maior = num
    elif num<menor:
        menor = num
print(maior)
print(menor)
