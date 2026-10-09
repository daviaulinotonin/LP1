def data (dia,mes,ano):
    if mes == 1:
        return (f'{dia} de Janeiro de {ano}')
    elif mes == 2:
        return (f'{dia} de Fevereiro de {ano}')
    elif mes == 3:
        return (f'{dia} de Março de {ano}')
    elif mes == 4:
        return (f'{dia} de Abril de {ano}')
    elif mes == 5:
        return (f'{dia} de Maio de {ano}')
    elif mes == 6:
        return (f'{dia} de Junho de {ano}')
    elif mes == 7:
        return (f'{dia} de Julho de {ano}')
    elif mes == 8:
        return (f'{dia} de Agosto de {ano}')
    elif mes == 9:
        return (f'{dia} de Setembro de {ano}')
    elif mes == 10:
        return (f'{dia} de Outubro de {ano}')
    elif mes == 11:
        return (f'{dia} de Novembro de {ano}')
    elif mes == 12:
        return (f'{dia} de Dezembro de {ano}')
    else:
        return 'Mês inválido.'
dia = int(input('Informe o dia \n> '))
mes = int(input('Informe o mês \n> '))
ano = int(input('Informe o ano \n> '))
print(data(dia,mes,ano))