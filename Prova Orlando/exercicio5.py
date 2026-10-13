print('|------------------------------------------------------------------------------------------|\n' \
      '| Código do Cargo |          Cargo          | Salário Base (R$) | Benefícios | Imposto (%) |\n' \
      '|-----------------|-------------------------|-------------------|------------|-------------|\n' \
      '|        1        | Auxiliar Administrativo | 2.200,00          | 350,00     | 7.5%        |\n' \
      '|        2        | Técnico de TI           | 3.520,00          | 450,00     | 9%          |\n' \
      '|        3        | Analista                | 4.400,00          | 500,00     | 11%         |\n' \
      '|        4        | Coordenador             | 6.600,00          | 800,00     | 14%         |\n' \
      '|        5        | Gerente                 | 8.800,00          | 1.200,00   | 18%         |\n' \
      '|------------------------------------------------------------------------------------------|')

quantidade_funcionarios = int(input('Informe a quantidade de funcionários: '))
total_folha_pagamento = 0
contador_funcionario = 0

for funcionario in range(quantidade_funcionarios):
    nome = input('Digite o nome do funcionário: ')
    codigo = int(input('Digite o código do cargo do funcionário: '))
    if codigo <1 or codigo >5: 
    #está ignorando o funcionário de código inválido, porém não consegui encontrar uma forma de repetir esta iteração sem utilizar algo que não tenhamos visto em aula
        print('Código inválido')
    hora_extra = int(input('Digite quantas horas extras tem o funcionário: '))

    if codigo == 1:
        salario_base = 2200
        beneficio = 350
        percentual_imposto = .075
        valor_hora = salario_base/220
        valor_extra = valor_hora * hora_extra * 1.5
        imposto = (salario_base + valor_extra) * percentual_imposto
        salario_liquido = salario_base + valor_extra + beneficio - imposto
        total_folha_pagamento += salario_liquido
        contador_funcionario += 1
        cargo = 'Auxiliar Administrativo'
        print(f'{nome}, {cargo.lower()} tem salário líquido de R${salario_liquido:.2f}')
    
    elif codigo == 2:
        salario_base = 4400
        beneficio = 500
        percentual_imposto = .11
        valor_hora = salario_base/220
        valor_extra = valor_hora * hora_extra * 1.5
        imposto = (salario_base + valor_extra) * percentual_imposto
        salario_liquido = salario_base + valor_extra + beneficio - imposto
        total_folha_pagamento += salario_liquido
        contador_funcionario += 1
        cargo = 'Técnico de TI'
        print(f'Como {cargo.lower()} seu salário líquido é de R${salario_liquido:.2f}')
    
    elif codigo == 3:
        salario_base = 2200
        beneficio = 350
        percentual_imposto = .075
        valor_hora = salario_base/220
        valor_extra = valor_hora * hora_extra * 1.5
        imposto = (salario_base + valor_extra) * percentual_imposto
        salario_liquido = salario_base + valor_extra + beneficio - imposto
        total_folha_pagamento += salario_liquido
        contador_funcionario += 1
        cargo = 'Analista'
        print(f'Como {cargo.lower()} seu salário líquido é de R${salario_liquido:.2f}')
    
    elif codigo == 4:
        salario_base = 6600
        beneficio = 800
        percentual_imposto = .14
        valor_hora = salario_base/220
        valor_extra = valor_hora * hora_extra * 1.5
        imposto = (salario_base + valor_extra) * percentual_imposto
        salario_liquido = salario_base + valor_extra + beneficio - imposto
        total_folha_pagamento += salario_liquido
        contador_funcionario += 1
        cargo = 'Coordenador'
        print(f'Como {cargo.lower()} seu salário líquido é de R${salario_liquido:.2f}')
    
    elif codigo == 5:
        salario_base = 8800
        beneficio = 1200
        percentual_imposto = .18
        valor_hora = salario_base/220
        valor_extra = valor_hora * hora_extra * 1.5
        imposto = (salario_base + valor_extra) * percentual_imposto
        salario_liquido = salario_base + valor_extra + beneficio - imposto
        total_folha_pagamento += salario_liquido
        contador_funcionario += 1
        cargo = 'Gerente'
        print(f'Como {cargo.lower()} seu salário líquido é de R${salario_liquido:.2f}')   
     
print(f'{contador_funcionario} funcionários estão nesta folha de pagamento')     
print(f'O total a ser pago nesta folha de pagamento é de R${total_folha_pagamento}')