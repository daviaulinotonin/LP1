num = int(input('Digite um número '))
fat = 1
for i in range(num,1,-1):
    fat *= i
    print(f'{fat}*{i-1}')
print(f'{num}! é igual a {fat}')