def calcular_desconto(valor, percentual=10):
    desconto = valor * (percentual / 100)
    return valor - desconto
print(calcular_desconto(100))
print(calcular_desconto(250,20))