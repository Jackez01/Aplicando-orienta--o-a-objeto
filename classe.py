class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        #isso faz com que o ativo fique privado
        self._ativo = False
        Restaurante.restaurantes.append(self)
        
        #serve para mostrar o testo em formato de string
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print (f'{'Nome do restaurante:'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'} ')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
    #modifica como o atributo vai ser lido
    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza express', 'Italiana')

Restaurante.listar_restaurantes()





