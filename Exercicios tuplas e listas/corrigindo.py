# O clube de atletismo Alura Runners organizou uma corrida e divulgou a
# lista com a classificação final dos participantes.
# Mas, um erro foi identificado: um dos nomes está incorreto.
# O organizador precisa de um programa que permita localizar o nome errado
# e substituí-lo pelo correto.

# Como você escreveria um programa que solicite o nome errado, o nome correto 
# e atualize a lista exibindo a nova classificação ao final?

lista_jogaadores = ['Bruno', ' Rogerio',  'Nicolle']
print(f'Lista original: {lista_jogaadores}')

nome_incorreto = input('Digite o nome incorreto: ')
if nome_incorreto in lista_jogaadores:
    nome_correto = input('Digite o nome correto: ')
    #pega a posição que o nome incorreto está
    posicao = lista_jogaadores.index(nome_incorreto)
    lista_jogaadores.remove(nome_incorreto)
    #adiciona o novo nome no mesmo local onde tirou o nome antigo
    lista_jogaadores.insert(posicao, nome_correto)
    print(f'O nome {nome_incorreto} foi removido e substituido por {nome_correto}')
    print(f'Lista atualizada {lista_jogaadores}')
else:
    print('Nome não encontrado')



