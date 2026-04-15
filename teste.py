dados = input('Digite os alunos separados por virgulas: ').split(', ')

for i in range(0, len(dados), 3):
    nome, idade, nota = dados [i], int (dados[i+1]), float(dados[i+2])
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'Nota: {nota}\n')

