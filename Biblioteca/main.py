# 7 Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos 
# da classe Livro e exiba a mensagem formatada utilizando o método str.

from biblioteca import Livro

livro_main1 = Livro("Python para Iniciantes", 2021, "Carlos Coder")
livro_main2 = Livro("Web Development Essentials", 2012, "Laura Developer")

print(livro_main1)
print(livro_main2)