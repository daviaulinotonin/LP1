# Desenvolva um programa que:
# Solicite a quantidade de dias que serão analisados 
# Para cada dia, leia a temperatura máxima registrada (em Cº)
# No final, exiba a maior temperatura, a menor temperatura, a média das temperaturas e quantos dias tiveram acima de 30º
# Observacão: Não utiliza max(), min(), nem listas; resolva com váriaveis de controle

dias = int(input('Quantos dias deseja medir a temperatura?\n>'))
if dias <=0:
    print('A quantidade precisa ser positiva.')
    print('Programa finalizado.')
elif dias >=1:
    soma_temp=0
    acima30=0

    for dia in range(1, dias+1):
        temp=int(input(f'Digite a temperatura em ºC do dia {dia}\n>'))
        soma_temp+=temp

        if temp>30:
            acima30=+1

        if dia == 1:
            maior = temp
            menor = temp
        else:
            if temp > maior:
                maior = temp
            if temp < menor:
                menor = temp

    media = soma_temp/dias
print(30*'-')
print(f'Estatísticas referente a temperatura medida em {dias} dia(s).')
print(f'A maior temperatura registrada é de {maior}ºC')
print(f'A menor temperatura registrada é de {menor}ºC')
print(f'A temperatura média é de {media}ºC')
print(f'{acima30} dia(s) atingiram uma temperatura superior a 30ºC')