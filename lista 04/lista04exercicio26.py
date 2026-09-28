def saudacao_por_hora(hora):
    if hora<12:
        return 'Bom dia'
    elif hora<18:
        return 'Boa tarde'
    elif hora<6 or hora>=18:
        return 'Boa noite'

hora = int(input('Que horas são? '))
print(saudacao_por_hora(hora))