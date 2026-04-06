# Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos.
# Um objeto é uma instância específica de uma classe, e as classes são utilizadas 
# para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.

# Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):

class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Nothing else metters'
musica1.artista = 'Metallica'
musica1.duracao = 3

print(vars(musica1))