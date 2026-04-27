# Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:

conjunto_laura = set(input('Lista de compras da Laura: ').split(', '))
conjunto_ana = set(input('Lista de compras da Ana: ').split(', '))

# Quais itens apareceram nas duas listas
itens_iguais = conjunto_ana.intersection(conjunto_laura)
print(f'Os itens iguais nas duas listas são: {', '.join(itens_iguais)}.')

# Quais foram exclusivos de Laura
diferenca_laura = conjunto_laura.difference(conjunto_ana)
print(f'Os itens que tem apenas na lista da Laura são: {', '.join(diferenca_laura)}.')

# Quais foram exclusivos da Ana
diferenca_ana = conjunto_ana.difference(conjunto_laura)
print(f'Os itens excluisvos apenas da lista da Ana são: {', '.join(diferenca_ana)}.')

# Escreva um programa que solicite as listas e mostre os resultados dessas comparações.
