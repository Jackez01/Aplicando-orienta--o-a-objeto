# 5 Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from biblioteca import Livro



livro1 = Livro('Algoritmos', 2015, 'Felipe Ferraz')
livro2 = Livro('Estruturação de dados', 2020, 'Rafael Alves')
livro3 = Livro('Assassins creed', 2012, 'Mike')

livro1.emprestar()
livro3.emprestar()

Livro.livros = [livro1, livro2, livro3]

print(livro1)
print(livro2)
print(livro3)



# 6 No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro 
# está disponível ou não após o empréstimo.


