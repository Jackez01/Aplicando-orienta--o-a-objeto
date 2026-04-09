# 1 Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. 
# Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular = '', saldo = float):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

# 2 Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem 
# formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f'Titular: {self.titular} | {self.saldo}'

# 3 Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. 
# Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    def ativar_conta(self):
        self._ativo = True
conta1 = ContaBancaria('lucas', 55879)
conta1.ativar_conta
print(conta1.ativar_conta())

# 4 Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. 
# Utilize propriedades, se necessário.
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
    
    def ativar_conta(self):
        self._ativo = True

# 5 Crie uma instância da classe e imprima o valor da propriedade titular.
conta2 = ContaBancaria('Flavio', 500)
print(f'Cliente da conta2 é {conta2.titular}')

# 6 Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos.
# Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, cliente = '', salario = float, endereco = ''):
        self.cliente = cliente
        self.salario = salario
        self.endereco = endereco
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta
cliente1 = ClienteBanco('Lucas', 7857, 'Rua franscico')
# 7 Crie um método de classe para a conta ClienteBanco.


