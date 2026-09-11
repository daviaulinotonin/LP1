valor = float(input('Digite o preço do produto R$'))
pag=input('Informe se o pagamento será pelo Pix ou cartão ')

if pag.lower() == 'pix':
  print(f'Total R${valor * 0.9}')

if pag.lower() == 'cartao' or pag.lower() == 'cartão':
  quant = int(input('Acima de 3 parcelas há um juros de 2% ao mês \nEm quantas parcelas você quer dividir a compra?  '))
  if quant > 3:
    parcela = valor / quant * 1.02
    print(f'Total: {quant} parcelas de R${parcela}')
    total = parcela * quant
    print(f'Custo final de R${total}')
  else:
    parcela = valor / quant
    print(f'Total: {quant} parcelas de R${parcela}')
