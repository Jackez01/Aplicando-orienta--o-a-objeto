# Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria. Ela precisa de um programa que permita cadastrar produtos em forma de dados estruturados. O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, exibir as informações cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.

dicionario = {}

for i in range(3):
    chave = input('Digite a chave do objeto: ')
    valor = input ('Digite o valor do objeto: ')
    
    dicionario[chave] = valor
    
    

print(f'Dicionario de produtos: {dicionario}')