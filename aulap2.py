#definindo classe livro
class livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor 
        self.ano = ano 
        
    # metodo __eq__ para comparar dos objetos livro 
    def __eq__(self, outro):
        if isinstance(outro, livro):
            return self.titulo == outo.titulo and salf.autor == outro.autor
       return False 
       
    # metodo __hash__ para permitir que objetos livros sejam adicionados a conjuntos
    def __hash__(self):
        return hash((self.titulo, self.autor))
        
    #metodo __repr__ para representar o objeto livro como basestring
    def __repr__(self):
        return f"livro(titulo='{self.titulo}', autor='{self.autor}', ano={self.ano})"
        
#criando três instancias da classe livro
livro1 = livro("1984", "George Orwell", 1949)
livro2 = livro("1984", "George Orwell", 1950)
livro3 = livro("Brave new Word", "Aldous Huxley", 1932)

#comprando os livros usando o metodo __eq__
print ("livro1 é igual a livro2?", livro1 == livro2) #deve retornar True
print ("livro1 é igual a livro3?", livro1 == livro3) #deve retornar False

#adicionando os livros a um conjunto 
conjunto_livros = {livro1, livro2, livro3}
print ("conjunto de livros:", conjunto_livros) #deve conter livro1 e livro3, pois livro1 e livro2 são iguais