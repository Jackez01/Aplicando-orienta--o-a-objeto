voluntarios = []


pedido = input('Digite o nome do novo voluntário: ')

while True:
    pedido = input('Digite o nome do novo voluntário: ')
    if pedido.lower() == 'sair':
        break
    voluntarios.append(pedido)


print(voluntarios)