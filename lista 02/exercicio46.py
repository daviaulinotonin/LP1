n1 = int(input('Informe a primeira nota do aluno '))
n2 = int(input('Informe a segunda nota do aluno '))
media = (n1+n2)/2
freq = float(input('Informe a frequência de presença do aluno '))
if freq >= 75:
  if media >=6:
    print(f'O aluno foi aprovado com média {media} e {freq}% de frequência nas aulas.')
  else:
    print(f'O aluno foi reprovado por nota. Pois sua média é {media}')
else:
  print(f'O aluno foi reprovado por faltas. Pois tem somente {freq}% de presença')