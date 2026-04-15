# Armano trabalha com a gestão de dois estoques de mercadorias que são 
# representados como tuplas. Agora, ele precisa criar um relatório unificado
# com os produtos dos dois estoques juntos.

# Para ajudá-lo, como você criaria um programa que ler as informações dos estoques
# e gera um relatório com todos os produtos juntos?

estoque1 = ['Maça', 'banana']
estoque2 = ['suco', 'leite']


#extend adiciona os itens individualmente, se usasse append iria ficar uma lista dentro de outra
#poderia usar tuplas também
estoque1.extend(estoque2)

print(estoque1)
