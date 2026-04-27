# Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade de um item específico no estoque. Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, atualizando essa informação no dicionário de estoque.

estoque = {'Caderno universitário': 50, 'Caneta azul': 120, 'Borracha branca': 30}

print(estoque)

atualizacao = input('Digite o item que você quer atualizar: ')
quantidade = int(input('Digite a nova quantidade: '))

if atualizacao in estoque:
    estoque[atualizacao] = quantidade

    print(f'A quantidade foi atualizada com sucesso!')
    print(estoque)
else: 
    print('Produto não encontrado!')