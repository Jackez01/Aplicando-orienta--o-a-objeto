# Implemente uma classe chamada Carro com os atributos básicos, 
# como modelo, cor e ano. 
# Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self,modelo ='', cor ='', ano = int ):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro(modelo = 'Peugeot', cor = 'Preto', ano = 2004)

print(vars(carro1))