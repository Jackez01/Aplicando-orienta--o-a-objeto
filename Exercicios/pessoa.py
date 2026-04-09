#  Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
class Pessoa:
    def __init__(self, nome ='', idade = 0, profissao = ''):
        self._nome = nome
        self._idade = idade
        self.profissao = profissao 
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
    def __str__(self):
        return f'Nome: {self._nome} | idade: {self._idade} | profissao: {self.profissao}'
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
    def aniversario(self):
        self._idade +=1
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada 
# com base na profissão da pessoa.
    def saudacao(self):
        if self.profissao:
            return f'Ola {self.profissao}'
        else:
            return f'Olá eu sou {self._nome}'
        

pessoa1 = Pessoa('Lucas', 24, 'Analista de suporte')


print(pessoa1.saudacao())