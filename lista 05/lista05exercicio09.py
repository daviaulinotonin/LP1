lista_notas = []
alunos = 2

for x in range(alunos):
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    notas = [n1,n2]
    lista_notas.append(notas)
print(lista_notas)

for aluno in lista_notas:
    media = sum(aluno)/len(aluno)
    print(media)