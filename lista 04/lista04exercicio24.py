def exibir_tabuada(numero,limite=11):
    for i in range(1,limite):
        mult = numero * i
        print(f'{numero} * {i} = {mult}')  
print(exibir_tabuada(5))
print(exibir_tabuada(7))
