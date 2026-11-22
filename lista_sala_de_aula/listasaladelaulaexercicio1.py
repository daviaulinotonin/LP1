def maximo(num1,num2):
    if num1>num2:
        return(num1)
    elif num2>num1:
        return(num2)

    elif num1==num2:
        return(num1 or num2)
print(maximo(5,6))

print(maximo(2,1))

print(maximo(7,7))
