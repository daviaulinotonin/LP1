nota = int(input('Informe a nota final do aluno '))
faltas = int(input('Informe o número de faltas do aluno '))
if faltas >= 15:
  print('Aluno reprovado por faltas')
elif nota >= 9:
  print('Aluno aprovado.')
  print('Conceito final: A')
elif nota >= 7:
  print('Aluno aprovado.')
  print('Conceito final: B')
elif nota >=5:
  print('Aluno aprovado.')
  print('Conceito final: C')
else:
  print('Aluno reprovado por nota.')
  print('Conceito final: D')
