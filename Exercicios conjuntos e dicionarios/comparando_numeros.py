# Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas. Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. Sua tarefa é criar um programa que realize essa operação.

equipe_a = set(["planejar reunião", "revisar documento", "testar sistema"])
equipe_b = set(["testar sistema", "implementar funcionalidade", "corrigir bug"])

#união dos dois conjntos
lista_completa = equipe_a.union(equipe_b)

remover = input('Digite o item que você quer remover: '.lower().split(', '))
lista_completa.discard(remover)

print(f'Lista final  das tarefas: {lista_completa}')