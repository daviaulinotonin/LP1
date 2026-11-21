# Observe o código abaixo. As funções media, extremos e ficha ainda não existem. 
# Você deve criá-las no lugar de Seu código aqui para que o programa funcione.
def media(*notas): #* permite com que a variável receba n valores
    if not notas:
        return 0
    return sum(notas)/len(notas)

def extremos(*valores):
    if not valores:
        return None
    menor = 0
    maior = 0
    for valor in valores:
        if valor < menor:
            menor = valor
        if valor > maior:
            maior = valor

print(media(7, 8.5, 6))
print(media(10, 9, 8, 7, 6))
print(media())

menor, maior = extremos(4, 9, 1, 7, 3)
print("Menor:", menor, "Maior:", maior)

# ficha(nome="Lucas", curso="ADS", semestre=2)
# ficha(nome="Mariana", curso="GTI", semestre=4, cidade="Rio Claro", turno="Noite")

# 2.1 Crie a função media(*notas), que recebe uma quantidade variável de notas e retorna a média
# delas. Se nenhuma nota for informada, a função deve retornar 0.

# 2.2 Crie a função extremos(*valores), que retorna uma tupla com o menor e o maior valor
# recebidos, nessa ordem. Não use as funções min() e max().

# 2.3 Crie a função ficha(**dados), que exibe a linha "= FICHA =", depois cada informação recebida
# no formato chave: valor (uma por linha) e, ao final, a mensagem "Total de campos: N".