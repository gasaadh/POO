from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def estudar(self):
        return f"{self.nome} está estudando {self.curso} na turma {self.turma}"

    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def matricula(self):
        print(f"O aluno {self.nome} acabou de fazer matricula")

class Professor(Pessoa):
    def estudar(self):
        return f'{self.nome} é especialista em {self.especialidade} no {self.nivel}'

    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} começou a dar aula")

class Funcionario(Pessoa):
    def estudar(self):
        return f"{self.nome} se especializa para a área de {self.setor}"

    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'O Funcionario {self.nome} acabou de bater ponto')