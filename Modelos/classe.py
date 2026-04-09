from Modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, _nome, categoria):
        #deixa a primeira letra maiuscula
        self._nome = _nome.title()
        self.categoria = categoria.upper()
        #isso faz com que o ativo fique privado
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
        #serve para mostrar o testo em formato de string
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print (f'{'nome do restaurante:'.ljust(25)} | {'Categoria'.ljust(25)} |{'Avaliação'.ljust(25)}| {'Status'} ')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} |{str(restaurante.media_avaliacao).ljust(25)}| {restaurante.ativo}')
    #modifica como o atributo vai ser lido
    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


    def receber_avaliacao(self, cliente, nota):
        #criando umobjeto
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma =sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma / quantidade_de_notas,1)
        return media



