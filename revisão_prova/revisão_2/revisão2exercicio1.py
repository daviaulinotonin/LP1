frase = "Python é uma linguagem de programação simples, poderosa e muito popular entre programadores"
vogais = "aeiouáéíóúâêôãõ"

total_palavras = 0
total_vogais = 0
palavra_mais_longa = ""
iniciais = ""

palavras=frase.replace(',','').split()
for letra in frase:
    if letra in vogais: #se a letra estiver dentro da variável vogais, aumenta o contador
        total_vogais+=1

for palavra in frase.split():
    total_palavras+=1

for palavra in palavras:
    iniciais += palavra[0].upper() #[0] seleciona o primeiro caractere
    if len(palavra) > len(palavra_mais_longa): #len verifica a quantidade de caracteres
        palavra_mais_longa = palavra

print("Total de palavras: " + str(total_palavras))
print("Total de vogais: " + str(total_vogais))
print("Palavra mais longa: " + palavra_mais_longa)
print("Iniciais: " + iniciais)