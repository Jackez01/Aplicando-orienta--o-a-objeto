# Nathalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de vendas organizados por categoria de produto. Cada categoria contém uma lista de dicionários representando as vendas individuais, com informações sobre o produto, a quantidade vendida e o valor unitário. Sua tarefa é criar um programa que exiba o total de vendas por categoria.

vendas = {
    'Eletronicos': [
        {'Produto': 'Smartphone', 'Quantidade': 5, 'Valor_unitario': 2000},
        {'Produto': 'Tablet', 'Quantidade': 3, 'Valor_unitario': 1500}
    ],
    'Eletrônicos': [
        {'Produto': 'Geladeira', 'Quantidade': 2, 'Valor_unitario': 3000},
        {'Produto': 'Micro-ondas', 'Quantidade': 4, 'Valor_unitario': 800}
    ],
    'Livros': [
        {'Produto': 'Livro A', 'Quantidade': 10, 'Valor_unitario': 50},
        {'Produto': 'Livro B', 'Quantidade': 5, 'Valor_unitario': 100}
    ]
}

print('Total de vendas por categoria:')

for categorias, itens in vendas.items():
    total = 0
    for item in itens:
        total += item['Quantidade'] * item['Valor_unitario:.2f']
    print(f'{categorias}: {total}')