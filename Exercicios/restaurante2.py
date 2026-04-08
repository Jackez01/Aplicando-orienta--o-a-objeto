# 1. Crie uma classe chamada Restaurante com os atributos nome,
# categoria, ativo e crie mais 2 atributos. 
# Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self, nome ='', categoria = '', ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

restaurante_centro = Restaurante(nome = 'Central Dog', categoria  = 'Fast Food', ativo = False)

# 2. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como 
# parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
class Restaurante:
    def __init__(self, nome, categoria, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
novo_restaurante = Restaurante('Santa Monicaf', categoria= 'Fast Food')



# 3. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, 
# seja exibida uma mensagem formatada com o nome e a categoria. 
# Exiba essa mensagem para uma instância de restaurante.
def __str__(self):
    return f'{self.nome} | {self.categoria}'

# 4. Crie uma classe chamada Cliente e pense em 4 atributos. 
# Em seguida, instancie 3 objetos desta classe e atribua
# valores aos seus atributos através de um método construtor.
class Cliente:
    def __init__(self, nome = '', prioridade ='', gostos = '', numero = int):
        self.nome = nome
        self.prioridade = prioridade
        self.gostos = gostos
        self.numero = int

cliente_novo = Cliente(nome = 'Familia Geraldi', prioridade = 'Alta', gostos = 'Gourtmet', numero = 4)


print(vars(restaurante_centro))
