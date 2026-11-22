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

    
def confere_dia(dia):
    if dia <1 or dia >31:
        print('Dia inválido.')
        exit()

def confere_mes(mes):
    if mes <1 or mes >12:
        print('Mês inválido.')
        exit()

def confere_ano(ano):
    if ano <1:
        print('Ano inválido.')
        exit()
    
dia = int(input('Informe o dia \n> '))
confere_dia(dia)
mes = int(input('Informe o mês \n> '))
confere_mes(mes)
ano = int(input('Informe o ano \n> '))
confere_ano(ano)
print(data(dia,mes,ano))