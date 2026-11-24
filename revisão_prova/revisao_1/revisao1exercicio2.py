python = ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Ana", "Fábio",
"Gabriela", "Hugo", "Igor", "Júlia", "Carla"]

banco_dados = ["Bruno", "Carla", "Elisa", "Gabriela", "Igor",
"Karen", "Lucas", "Marina", "Bruno"]

redes = ["Carla", "Diego", "Elisa", "Igor", "Lucas",
"Nathan", "Olívia", "Pedro"]

conjunto_python = set(python)
conjunto_dados = set(banco_dados)
conjunto_redes = set(redes)

print(f'Os alunos matriculados nas três disciplinas são: {sorted(conjunto_python & conjunto_dados & conjunto_redes)}')
print(f'O total de alunos diferentes é de: {len(conjunto_python | conjunto_dados | conjunto_redes)} alunos')
print(f'{sorted(conjunto_python^conjunto_dados)} são os alunos que cursam Python ou Banco de dados, mas não os dois')
# Outra forma de realizar diferença simétrica
# print(conjunto_python.symmetric_difference(conjunto_dados))
print(f'Os alunos que cursam somente python são: {sorted(conjunto_python -  conjunto_dados -  conjunto_redes)}')