itens = int(input('Informe quantos produtos serão inseridos em sistema\n> '))

produtos = []

for item in range(itens):
    nome_produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço unitário de cada produto: '))
    estoque = int(input('Digite a quantidade de itens em estoque '))

    produto = {
        'nome_produto': nome_produto,
        'preco': preco,
        'estoque': estoque
    }
    total = preco * estoque
    if estoque <10:
        print(f'{nome_produto} está com estoque baixo!')
    print(f'Valor total em estoque R${total:.2f}\n')
    produtos.append(produto)

