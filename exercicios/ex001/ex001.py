class Cadastro:
    def __init__(self, nome = "vazio", idade = 0):  #Método Construtor
        #Atributos de Instância
        self.nome = nome
        self.idade = idade


        #Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos"

#Declaração de Objeto
c1 = Cadastro('Gabriel', 20)
print(c1.mensagem())
