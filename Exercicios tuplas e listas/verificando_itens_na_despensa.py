# Roberto está organizando sua despensa e quer verificar se determinados itens já estão 
# armazenados antes de adicioná-los à lista de compras.

# Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na 
# lista de itens disponíveis na despensa. Caso o item não esteja na lista,
# o programa deve informar que ele precisa ser comprado.

lista = ['uva', 'maçâ', 'queijo']

def verificador_itens(item):
        if item in lista:
            print('Esse Item já tem na despensa')
        else:
            print('Esse item não existe na despensa, compre no mercado')
item_desejado = input('Digite o item que você quer verificar')

print(verificador_itens(item_desejado))