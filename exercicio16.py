nome = input('Informe seu nome ')
salario = float(input('Informe seu salário atual '))
porcentagem = int(input('Informe a porcentagem desejada para calcular um aumento '))
aumento = (salario*(porcentagem/100))+salario
print(nome.title() + ', se você receber um aumento de', str(porcentagem) + '%, seu novo salário será de R$' + str(aumento))
