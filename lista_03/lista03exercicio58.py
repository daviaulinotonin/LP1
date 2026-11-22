soma = 0
for dia in range (1,8):
    horas=int(input(f'Informe quantas horas foram trabalhadas no {dia}º dia: '))
    soma += horas
if soma <36:
    print('Carga horária semanal leve')
elif soma <44:
    print('Carga horária semanal moderada')
elif soma >=44:
    print('Carga horária semanal pesada')