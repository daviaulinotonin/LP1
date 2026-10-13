print('|------------------------------------------------------------------------------|\n' \
          '| Código do Cargo |    Cargo    | Salário Base (R$) | Benefícios | Imposto (%) |\n' \
          '|-----------------|-------------|-------------------|------------|-------------|\n' \
          '|        1        | Escrituário | 2.500,00          | 300,00     | 8%          |\n' \
          '|        2        | Secretário  | 3.200,00          | 450,00     | 10%         |\n' \
          '|        3        | Caixa       | 3.800,00          | 600,00     | 12%         |\n' \
          '|        4        | Gerente     | 7.500,00          | 1.000,00   | 15%         |\n' \
          '|        5        | Diretor     | 12.000,00         | 2.000,00   | 20%         |\n' \
          '|------------------------------------------------------------------------------|')
def calcula_salario(codigo):
    # salario liquido = salario base + beneficios - impostos
    if codigo == 1:
        salario_liquido =  (2500 + 300) * .92
        cargo = 'Escrituário'
        return(f'Como {cargo.lower()} seu salário líquido é de R${salario_liquido:.2f}')
    elif codigo == 2:
        salario_liquido = (3200 + 450) * .90
        cargo = 'Secretário'
        return(f'Como {cargo.lower()} seu salário líquido é de R${salario_liquido:.2f}')
    elif codigo == 3:
        salario_liquido = (3800 + 600) * .88
        cargo = 'Caixa'
        return(f'Como {cargo.lower()} seu salário líquido é de R${salario_liquido:.2f}')
    elif codigo == 4:
        salario_liquido = (7500 + 1000) * .85
        cargo = 'Gerente'
        return(f'Como {cargo.lower()} seu salário líquido é de R${salario_liquido:.2f}')
    elif codigo == 5:
        salario_liquido = (12000 + 2000) * .80
        cargo = 'Diretor'
        return(f'Como {cargo.lower()} seu salário líquido é de R${salario_liquido:.2f}')    
    else:
        return 'Código inválido'      
print(calcula_salario(1))
print(calcula_salario(2))
print(calcula_salario(3))
print(calcula_salario(4))
print(calcula_salario(5))
print(calcula_salario(0))