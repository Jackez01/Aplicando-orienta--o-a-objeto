# Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento. O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante. O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.

workshop = {'carla', 'Aice', 'Bruno', 'Diego'}
workshop2 = {'Fernanda', 'Gustavo', 'Helena'}

deletar = input('Digite o nome que você quer deletar: ')
del workshop[deletar]

print(', '.join(workshop))
print(', '.join(workshop2))