class Cadastro:
    """
    Essa classe cria um novo objeto de cadastro,
    possuindo nome e idade

    Para criar um novo cadastro, use
    variavel = Cadastro('nome',idade)
    """
    def __init__(self, nome = "vazio", idade = 0):  #Método Construtor
        #Atributos de Instância
        self.nome = nome
        self.idade = idade


        #Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"

    def __getstate__(self):
        return f"Nome: {self.nome}, idade:  {self.idade}"

#Declaração de Objeto
c1 = Cadastro('Gabriel', 20)

#Dunder = Double Underline __
#Docstring

print(c1)