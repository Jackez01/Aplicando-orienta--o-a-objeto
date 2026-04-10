# 1 Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. 
# Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    def __init__(self, titulo = '', ano_publicacao = int, autor = ''):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.autor = autor
        self.disponivel = True

# 2 Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, 
# autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f'Título: {self.titulo.ljust(25)} | Autor: {self.autor.ljust(25)} | Publicado em: {self.ano_publicacao} | Disponível: {self.disponivel}'




# 3 Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
# Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar(self):
        self.disponivel = False


# 4 Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano 
# como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis
    
ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")







