# Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos
# voluntários que vão ajudar na ação. À medida que os voluntários se inscrevem, seus nomes devem ser
# adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.

# Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

voluntarios = []



while pedido == 'sair':
    pedido = input('Digite o nome do novo voluntário: ')
    voluntarios.append(pedido)

print(voluntarios)
