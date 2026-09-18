def multiplo(num1,num2):
   if num1 % num2 == 0:
    return True
   if not num1 % num2 == 0:
     return False
mult = multiplo(8,4)
print(mult)

mult = multiplo(7,4)
print(mult)

mult = multiplo(5,5)
print(mult)