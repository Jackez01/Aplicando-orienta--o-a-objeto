# Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões faz parte das permissões principais de um sistema. Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.

caso_principal = set(p.strip() for p in input('Permissões principais: ').lower().split(', '))
caso_solicitados = set(p.strip() for p in input('Permissões Solicitadas: ').lower().split(', '))


permissoes = caso_solicitados.issubset(caso_principal)

if permissoes:
    print('As permissões solicitadas fazem parte das solicitações principais.')
else:
    print('As solcitações não fazem parte das solicitações requeridas.')