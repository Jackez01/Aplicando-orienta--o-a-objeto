# Uma escola realizou um concurso de redação, e o próximo passo é organizar 
# as notas dos participantes para definir a ordem de premiação. Para garantir transparência,
# as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.

# Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de 
# todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.

notas = [60, 80, 50, 94, 20]

# sort() modifica a propria lista
#numeros.sort(reverse=True) ordena decrescente

# existe sorted também que cria uma nova lista
notas.sort()
print(f'As notas em ordem crescente fica: {notas}')

