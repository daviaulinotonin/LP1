#num = int(input('Digite um número positivo '))
#fat = 1
#cont = 1
#while cont <= num:
#  fat *= cont
#  cont += 1
#print(fat)

num = int(input('Digite um número positivo '))
fat = 1
cont = num
while cont > 1:
  fat *= cont
  cont -= 1
print(fat)