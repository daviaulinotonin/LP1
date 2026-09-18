def maximo(num1,num2):
    if num1>num2:
        return(num1)
    elif num2>num1:
        return(num2)

    elif num1==num2:
        return(num1 or num2)
maior = maximo(5,6)
print(maior)

maior = maximo(2,1)
print(maior)

maior = maximo(7,7)
print(maior)