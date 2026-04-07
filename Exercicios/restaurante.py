class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = ''
restaurante_pizza = Restaurante()





#1 Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria = 'Italiana'
# 2 Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(restaurante_praca.nome)
# 3 Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_praca.ativo:
    print('O restaurante está ativo')
else: 
    print('O restaurante não está ativo.')

# 4 Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria
# 5 Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistro'
# 6 Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza PLace'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = False
# 7 Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
    print('É fastfood')
else:
    print('A categoria não é fast food')
# 8 Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True
# 9 Imprima no console o nome e a categoria da instância restaurante_praca.
print(restaurante_pizza.nome, restaurante_pizza.categoria)