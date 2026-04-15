# Camila adora receber amigos para jantares temáticos.
# Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, 
# mas ainda precisa fazer ajustes na lista de convidados.
# Camila quer adicionar novos nomes e organizá-los em posições específicas.

# Como você criaria um programa que mostre a lista inicial, permita a inserção 
# de um novo nome em uma posição escolhida e exiba a lista atualizada?


lista_convidados = ['Lucas', 'João', 'Ana']


print(f'Lista de convidados atual {lista_convidados}')

while True:
    insercao = input('Digite o novo nome que deseja adicionar: ')

    if insercao == 'sair':
        break
    posicao = int(input('Digite a posição que você quer adicionar: '))

# -1 para igualar a posição da lista para o usuário
    lista_convidados.insert(posicao -1, insercao)

print(lista_convidados)